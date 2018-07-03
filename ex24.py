poem="""\tThe lovely world
with logic so firmly planted
cannot discern
the needs of love nor comprehend passion from intuition and requires an explanation
\t\t where there is none."""

print "Let's practice everything."
print "you'd need to know 'bout escapes with \\ that do newlines and \t tabs."
print "-----------------"

print poem

print "-----------------"

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars, crates

start_point=10000
beans,jars,crates=secret_formula(start_point)
print "With a staring poing of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans,jars,crates)