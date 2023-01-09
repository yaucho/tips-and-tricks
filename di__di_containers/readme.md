<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Dependency_Injection_0"></a>Dependency Injection</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="Concept_1"></a>Concept:</h2>
<p class="has-line-data" data-line-start="2" data-line-end="4">Dependency injection is a style of object customization in which the fields of an object are set by an external entity. In other words, objects are configured by external objects.<br>
For example:</p>
<pre><code class="has-line-data" data-line-start="5" data-line-end="9">class Mail:
    def __init__(self, provider: MailProvider):
        self._provider = provider
</code></pre>
<p class="has-line-data" data-line-start="9" data-line-end="11">That is, the Mail class is provider-specific. And instead of initializing a specific provider internally, it is passed externally.<br>
Proc:</p>
<ul>
<li class="has-line-data" data-line-start="11" data-line-end="12">We are customizing way of providing mails via setting provider atribute from outside.</li>
<li class="has-line-data" data-line-start="12" data-line-end="14">It is also usefull in tests because we can pass some Mock object to Mail and test only Mail class logic.</li>
</ul>
<p class="has-line-data" data-line-start="14" data-line-end="15">Cons:</p>
<ul>
<li class="has-line-data" data-line-start="15" data-line-end="17">There can be several parts in the code from where we need to send mail. And if we want to change the mail provider, we must do this every time mail is initialized.</li>
</ul>
<h1 class="code-line" data-line-start=17 data-line-end=18 ><a id="DI_Container_17"></a>DI Container</h1>
<p class="has-line-data" data-line-start="18" data-line-end="19">This is the container that manages the injections. lol.</p>
<p class="has-line-data" data-line-start="20" data-line-end="21">If all components in your system have their own dependencies, then somewhere in the system some class or factory must know what to inject into all these components. That’s what the DI container does. The reason it’s called a “container” and not a “factory” is because the container usually takes responsibility for more than just creating instances and injecting dependencies.</p>
<p class="has-line-data" data-line-start="22" data-line-end="24">When you configure a DI container, you define which components it should be able to instantiate and which dependencies to inject into each component. Also, you can usually set the instantiation mode for each component. For example, should a new instance be created each time? Or should the same component instance be reused (singleton) everywhere it is injected?<br>
Some of these benefits:</p>
<ul>
<li class="has-line-data" data-line-start="24" data-line-end="25">Less dependencies</li>
<li class="has-line-data" data-line-start="25" data-line-end="26">Less “carrying around” of dependencies</li>
<li class="has-line-data" data-line-start="26" data-line-end="27">Code is easier to reuse</li>
<li class="has-line-data" data-line-start="27" data-line-end="28">Code is easier to test</li>
<li class="has-line-data" data-line-start="28" data-line-end="30">Code is easier to read</li>
</ul>
<p class="has-line-data" data-line-start="30" data-line-end="31">Using in Python with library <a href="https://github.com/bobthemighty/punq">punq</a>.</p>
<p class="has-line-data" data-line-start="32" data-line-end="34">Just register a container with relation what mail provider to use in MailProvider class.<br>
And call container.resolve(MailProvider) to get registered mail provider.</p>
<p class="has-line-data" data-line-start="36" data-line-end="38">Source:<br>
<a href="https://www.youtube.com/watch?v=haqLhNN5ZdY&amp;ab_channel=%D0%94%D0%B8%D0%B4%D0%B6%D0%B8%D1%82%D0%B0%D0%BB%D0%B8%D0%B7%D0%B8%D1%80%D1%83%D0%B9%21">https://www.youtube.com/watch?v=haqLhNN5ZdY&amp;ab_channel=Диджитализируй!</a></p>