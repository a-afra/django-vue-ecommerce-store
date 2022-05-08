<template>
<section class="hero is-fullheight">
		<div class="hero-body">
			<div class="container has-text-centered">
				<div class="columns is-8 is-variable">
					<div class="column is-two-thirds has-text-left">
						<h1 class="title is-1">About Me</h1>
						<p class="is-size-4">Hi everyone!</p>
            <p class="is-size-4">I did this project to test my Django and Web Development skills.</p>
            <p class="is-size-4">I'm not a Frontend developer!</p>
            <p class="is-size-4">So for the vue.js part I used the help of
              <a href="https://www.youtube.com/c/CodeWithStein">codeWithStein</a> tutorials.</p>
            <p class="is-size-4">Finally, feel free to contact me using the following links!</p>

						<div class="social-media">
							<a href="https://www.linkedin.com/in/alireza-afra-b89a18181/" target="_blank" class="button is-light is-large mr-4 mt-5">
                <i class="fa fa-linkedin" aria-hidden="true"></i>
              </a>
							<a href="https://github.com/a-afra" target="_blank" class="button is-light is-large mt-5">
                <i class="fa fa-github " aria-hidden="true"></i>
              </a>
						</div>
					</div>
					<div class="column is-one-third has-text-left">
						<div class="field">
							<label class="label">Name</label>
							<div class="control">
								<input class="input is-medium" type="text">
							</div>
						</div>
						<div class="field">
							<label class="label">Email</label>
							<div class="control">
								<input class="input is-medium" type="text">
							</div>
						</div>
						<div class="field">
							<label class="label">Message</label>
							<div class="control">
								<textarea class="textarea is-medium"></textarea>
							</div>
						</div>
						<div class="control">
							<button type="submit" class="button is-info is-fullwidth has-text-weight-medium is-medium">Send Message</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
export default {
  name: "AboutMeView"
}
</script>

<style scoped>

</style>