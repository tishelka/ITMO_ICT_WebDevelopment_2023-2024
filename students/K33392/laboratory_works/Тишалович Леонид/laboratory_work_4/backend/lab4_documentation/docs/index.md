# Лабораторная работа №4

## Общая инфрмация

Для реализации фронтенда был использован TypeScript, React, CSS-Modules (SASS). Для роутинга использовался React Router, для отправки запросов на бэкенд - axios.

## SignInPage.tsx

Функция для регистрации

```
const handleRegister = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/auth/users/", {
        email: email,
        username: userName,
        password: password,
      });

      if (response.status === 201) {
        const userId = response.data.id;
        localStorage.setItem("authToken", response.data.auth_token);
        localStorage.setItem("userId", userId);
        localStorage.setItem("username", userName);
        alert("Регистрация успешна");
        navigate("/main");
      }
    } catch (error) {
      console.error("Ошибка при регистрации:", error);
    }
  };
```

Функция для логина

```
const handleLogin = async () => {
    try {
      const loginResponse = await axios.post(
        "http://127.0.0.1:8000/auth/token/login/",
        {
          username: userName,
          password: password,
        }
      );

      if (loginResponse.status === 200) {
        localStorage.setItem("authToken", loginResponse.data.auth_token);
        const userResponse = await axios.get(
          "http://127.0.0.1:8000/auth/users/me/",
          {
            headers: {
              Authorization: `Token ${loginResponse.data.auth_token}`,
            },
          }
        );

        if (userResponse.status === 200) {
          const userId = userResponse.data.id;
          localStorage.setItem("userId", userId);
          localStorage.setItem("username", userName);
          alert("Вход выполнен успешно");
          navigate("/main");
        }
      }
    } catch (error) {
      console.error("Ошибка при входе:", error);
    }
  };
```

## MainPage.tsx

Функци для получения конференций пользователя и других пользователей с бэкенда

```
useEffect(() => {
    const fetchConferences = async () => {
      try {
        if (!authToken) {
          console.error("Токен отсутствует в localStorage");
          return;
        }
        const headers = {
          Authorization: `Token ${authToken}`,
        };

        const response = await axios.get(
          "http://127.0.0.1:8000/main/conferences/",
          { headers }
        );

        if (response.status === 200) {
          const myConfs = response.data.filter(
            (conference: ConferenceData) => conference.author === username
          );
          const otherConfs = response.data.filter(
            (conference: ConferenceData) => conference.author !== username
          );

          setMyConferences(myConfs);
          setConferences(otherConfs);
        }
      } catch (error) {
        console.error("Ошибка при получении списка конференций:", error);
      }
    };

    fetchConferences();
  }, [authToken, username]);
```

## ConferenceCreatePage.tsx

Функция для получения тем с бэкенда (для последующего его использования при создании конференции)

```
  useEffect(() => {
    const fetchTopics = async () => {
      try {
        const headers = {
          Authorization: `Token ${authToken}`,
        };

        const response = await axios.get("http://127.0.0.1:8000/main/topics/", {
          headers,
        });
        setTopics(response.data);
      } catch (error) {
        console.error("Ошибка при загрузке тем:", error);
      }
    };

    fetchTopics();
  }, [authToken]);
```

Функция для отправки формы создания конференции

```
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const headers = {
      Authorization: `Token ${authToken}`,
    };

    const conferenceData = {
      title,
      location,
      start_date: startDate,
      end_date: endDate,
      description,
      participation_conditions: conditions,
      topics: selectedTopic,
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/main/conferences/",
        conferenceData,
        { headers }
      );
      if (response.status === 201) {
        alert("Конференция успешно создана");
      }
    } catch (error) {
      console.error("Ошибка при создании конференции:", error);
    }
  };
```

## ConferencePage.tsx

Функция для получения деталей конференции и отзывов с бэкенда

```
  useEffect(() => {
    const fetchConferenceDetails = async () => {
      try {
        const headers = {
          Authorization: `Token ${authToken}`,
        };
        const response = await axios.get(
          `http://127.0.0.1:8000/main/conferences/${id}/`,
          { headers }
        );

        if (response.status === 200) {
          setConference(response.data);
        }
      } catch (error) {
        console.error("Ошибка при получении информации о конференции:", error);
      }
    };

    const fetchReviews = async () => {
      try {
        const headers = {
          Authorization: `Token ${authToken}`,
        };
        const response = await axios.get(
          `http://127.0.0.1:8000/main/reviews/`,
          { headers }
        );

        if (response.status === 200) {
          const filteredReviews = response.data.filter(
            (review: Review) => review.conference.id === Number(id)
          );
          setReviews(filteredReviews);
        }
      } catch (error) {
        console.error("Ошибка при получении отзывов:", error);
      }
    };

    fetchConferenceDetails();
    fetchReviews();
  }, [id, authToken]);
```

Функция для отправки формы написания отзыва

```
  const handleReviewSubmit = async (
    event: React.FormEvent<HTMLFormElement>
  ) => {
    event.preventDefault();
    try {
      const headers = {
        Authorization: `Token ${authToken}`,
      };

      const currentDate = new Date().toISOString().split("T")[0];

      const reviewData = {
        text: reviewText,
        comment_text: commentText,
        rating: reviewRating,
        conference: Number(id),
        comment_date: currentDate,
        user: userId,
      };
      const response = await axios.post(
        `http://127.0.0.1:8000/main/reviews/`,
        reviewData,
        { headers }
      );
      if (response.status === 201) {
        setReviews([...reviews, response.data]);
        setReviewText("");
        setCommentText("");
        setReviewRating(1);
      }
    } catch (error) {
      console.error("Ошибка при отправке отзыва:", error);
    }
  };
```

## Conference.tsx

Функция для регистрации пользователя на конференцию

```
  const handleRegistration = async () => {
    try {
      const headers = {
        Authorization: `Token ${authToken}`,
      };

      const registrationData = {
        user: userId,
        conference: id,
        topic: topics[0].id,
      };

      const response = await axios.post(
        "http://127.0.0.1:8000/main/registrations/",
        registrationData,
        { headers }
      );

      if (response.status === 201) {
        alert("Регистрация на конференцию выполнена успешно!");
      }
    } catch (error) {
      console.error("Ошибка при регистрации на конференцию:", error);
      alert("Ошибка при регистрации!");
    }
  };
```
