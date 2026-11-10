# Schema inspection

Resolve the exact message and namespace. Use structure.md for roots and dependencies, then focused type pages. Search the exact message plus type or XML name. For field-path questions, follow only the needed enclosing types and dependency declarations.

Preserve:
- QName, element/attribute spelling, declaration order and source location.
- Enclosing sequence/all/choice cardinality as well as member cardinality.
- Optionality, nillability, defaults/fixed values, qualification and attribute use.
- Inheritance, restrictions, enumerations, patterns, length/numeric facets, wildcards and identity constraints where applicable.
- The distinction between literal source attributes and effective omitted defaults.

A choice does not make each member independently required. A leaf's local occurrence does not necessarily establish its effective requirement on the full path. Reuse references for recursive types; do not expand them infinitely.

For an exact type name, start with --limit 1 in the scoped search. Read the section named Complete compositor, member and restriction reference first; use outline if its heading differs. Read Reuse and recursion only when enclosing usage matters. Prefer these focused sections over loading the full type page and its duplicate literal declaration. Inspect their literal XML or the included XSD when needed for an exact structural claim. Never fetch an import or external schema. If a supplied dependency is unavailable, qualify the result.

A documentation-only message has no supplied schema; do not synthesize one or assume its namespace. An External...Code type is not a current enumeration. Consult the separate code-publication module for values.

Cite exact message, namespace, type/path, source ID and declaration line. Keep MDR business constraints distinct. XML generation and executable instance validation are outside this research skill's scope.
