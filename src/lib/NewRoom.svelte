<script>
  import { isNewRoom } from "../store/store";
  import { socket } from "../store/socketio";

  let username = "";
  function onSubmit(e) {
    e.preventDefault();
    isNewRoom.set(true);
    socket.emit("create_room", { username: username });
  }

  function isValid(username) {
    if (username.length < 2) {
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
    <br />
    <button disabled={isValid(username)}>Create</button>
  </form>
</div>

<style>
  .join-form > * {
    padding: 10px 10px;
    margin: 0 0 10px 0;
  }

  .join-form button {
    padding: 5px 5px;
  }
</style>
