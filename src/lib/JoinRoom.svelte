<script>
  let username = "";
  let roomID = "";
  function onSubmit(e) {
    e.preventDefault();
    console.log("submitted");
  }

  function isValid(roomID) {
    if (roomID.length < 8) {
      return true;
    } else false;
  }
</script>

<div class="select-username">
  <form on:submit={onSubmit} class="join-form">
    <input
      v-model="username"
      bind:value={username}
      class="username"
      placeholder="Your Username..."
    />
    <input
      v-model="roomID"
      class="room-id"
      bind:value={roomID}
      placeholder="Room ID..."
    />
    <br />
    <button disabled={isValid(roomID)}>Join</button>
  </form>
</div>

<style>
  .join-form {
    margin: auto;
    width: 50%;
  }

  .join-form > * {
    padding: 10px 10px;
    margin: 0 0 5px 0;
  }

  .join-form button {
    padding: 5px 5px;
  }
</style>
