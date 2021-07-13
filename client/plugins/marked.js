import marked from "marked";
import highlightjs from "highlight.js";
import DOMPurify from "dompurify";

export default ({app}, inject) => {
	inject("marked", (text) => {
		marked.setOptions({
			breaks: true,
			langPrefix: '',
			highlight (code, lang) {
				return highlightjs.highlightAuto(code, [lang]).value
			},
		})
		return DOMPurify.sanitize(marked(text))
	})
}
