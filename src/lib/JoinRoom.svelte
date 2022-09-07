<script>
  import { isJoinRoom } from "../store/store";
  import { socket } from "../store/socketio";

  let join_status;
  socket.on("join_status", (data) => {
    console.log("error", data);
    join_status = data.status;
    if (join_status == 200) isJoinRoom.set(true);
    else isJoinRoom.set(false);
  });

  let username = "";
  let roomID = "";

  function onSubmit(e) {
    e.preventDefault();
    socket.emit("join_room", { username: username, roomId: roomID });
  }

  function isValid(roomID) {
    if (roomID.length < 4) {
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
