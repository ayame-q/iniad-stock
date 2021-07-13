export default {
	// Server-side rendering Mode: https://go.nuxtjs.dev/ssr-mode
	ssr: false,

	// Global page headers: https://go.nuxtjs.dev/config-head
	head: {
		title: "INIAD Stock",
		titleTemplate: "%s - INIAD Stock",
		htmlAttrs: {
			lang: "ja",
		},
		meta: [
			{charset: "utf-8"},
			{name: "viewport", content: "width=device-width, initial-scale=1"},
			{hid: "description", name: "description", content: ""},
			{name: "format-detection", content: "telephone=no"},
		],
		link: [
			{rel: "icon", type: "image/x-icon", href: "/favicon.ico"},
		],
	},

	// Global CSS: https://go.nuxtjs.dev/config-css
	css: [],

	// Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
	plugins: [
		{ src: '@/plugins/vue-easymde', ssr: false },
		{ src: '@/plugins/vue-tags-input', ssr: false },
		{ src: '@/plugins/vue-js-modal.js'},
		{ src: '@/plugins/marked.js' }
	],

	// Auto import components: https://go.nuxtjs.dev/config-components
	components: true,

	// Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
	buildModules: [
		// https://go.nuxtjs.dev/eslint
		"@nuxtjs/eslint-module",
		// https://go.nuxtjs.dev/stylelint
		"@nuxtjs/stylelint-module",
		// https://github.com/nuxt-community/style-resources-module
		"@nuxtjs/style-resources",
	],

	// ESLint Configuration: https://github.com/nuxt-community/eslint-module
	eslint: {
		fix: true,
	},

	// StyleLint Configuration: https://github.com/nuxt-community/stylelint-module
	stylelint: {
		fix: true,
	},

	// Style Resources Configuration: https://github.com/nuxt-community/style-resources-module
	styleResources: {
		scss: ['@/assets/scss/*.scss'],
	},

	// Modules: https://go.nuxtjs.dev/config-modules
	modules: [
		// https://go.nuxtjs.dev/axios
		"@nuxtjs/axios",
	],

	// Axios module configuration: https://go.nuxtjs.dev/config-axios
	axios: {},

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {},
};
