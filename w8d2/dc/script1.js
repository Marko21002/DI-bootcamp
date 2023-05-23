const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];

   const usernames = [];
   const top_tier = [];
   var total = 0;

   gameInfo.forEach((info) => {
    if(info.score >5){
        top_tier.push(info.username)

    }
    usernames.push(info.username + "!");
    total += info.score
  });
  console.log(usernames)
  console.log(top_tier)
  console.log(total)
