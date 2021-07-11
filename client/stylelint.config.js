module.exports = {
	extends: [
		"stylelint-config-standard",
		'stylelint-config-recommended-scss',
	],
	// add your custom config here
	// https://stylelint.io/user-guide/configuration
	plugins: [
		'stylelint-scss',
	],
	rules: {
		indentation: "tab",
		"no-empty-source": [true, {severity: "warning"}],
		"block-no-empty": [true, {severity: "warning"}],
		"no-descending-specificity": null,
		'selector-pseudo-element-no-unknown': [
			true,
			{
				ignorePseudoElements: ['v-deep'],
			},
		],
	},
};
