// Part of Reactive collections for Hookless: https://hookless.machinezoo.com/collections
import com.machinezoo.stagean.*;

/**
 * Reactive wrappers for {@link java.util} collections.
 * See {@link com.machinezoo.hookless.collections.ReactiveCollections}.
 * 
 * @see <a href="https://hookless.machinezoo.com/collections">Reactive collections homepage</a>
 */
@DraftApi
@StubDocs
@NoTests
module com.machinezoo.hookless.collections {
	exports com.machinezoo.hookless.collections;
	requires com.machinezoo.hookless;
	requires com.machinezoo.stagean;
}
