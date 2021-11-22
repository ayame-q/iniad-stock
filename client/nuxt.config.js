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
		// https://http.nuxtjs.org/
		'@nuxt/http',
		// https://github.com/microcipcip/cookie-universal/tree/master/packages/cookie-universal-nuxt
		'cookie-universal-nuxt',
	],

	// http module configuration: https://http.nuxtjs.org/options
	http: {
		baseURL: "http://127.0.0.1"
	},

	// Middlewares: https://nuxtjs.org/ja/docs/directory-structure/middleware/
	router: {
		middleware: [
			"getMyUser",
			"initializeMyUser"
		],
	},

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {
		// Vue Svg Loader https://github.com/visualfanatic/vue-svg-loader
		extend: (config) => {
			const svgRule = config.module.rules.find(rule => rule.test.test('.svg'));

			svgRule.test = /\.(png|jpe?g|gif|webp)$/;

			config.module.rules.push({
				test: /\.svg$/,
				oneOf: [
					{
						resourceQuery: /inline/,
						use: [
							'babel-loader',
							'vue-svg-loader',
						],
					},
					{
						loader: 'file-loader',
						query: {
							name: 'assets/[name].[hash:8].[ext]',
						},
					},
				],
			});
		},
	},
};
