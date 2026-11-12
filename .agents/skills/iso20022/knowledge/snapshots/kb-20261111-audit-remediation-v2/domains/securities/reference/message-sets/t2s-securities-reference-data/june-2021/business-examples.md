---
template: false
document_kind: "business-examples-index"
review_status: "needs-review"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
domain: "securities"
message_sets: ["t2s-securities-reference-data"]
message_ids: ["reda.006.001.01", "reda.007.001.01", "reda.008.001.01", "reda.009.001.01", "reda.010.001.01", "reda.012.001.01", "reda.013.001.01", "reda.029.001.01", "reda.030.001.01", "reda.033.001.01", "reda.034.001.01"]
limitations: ["Source XML examples are preserved as supplied. Excerpts do not consistently declare namespaces; no full-document schema-validation pass is inferred.", "Companion Part2 is March2024, separately recorded under issue-000010.", "Completed Security Creation Status Advice example P398–P418 is not well-formed: opening SctyCreStsAdvc is absent while its closing tag appears at P417; directly confirmed on Word page32. Source remains unchanged (issue-000051)."]
---

# Securities reference-data business examples

The source prints exact message identifiers in its business-example headings. Retrieve the focused source section to read its description and complete literal message instance; values, leading zeros and status/reason labels remain unchanged.

| Canonical definition | Exact heading locators | Focused source sections |
| --- | --- | --- |
| [reda.006.001.01](../../../messages/reda.006.001.01/index.md) | P320 | [section-0039](documents/src-000377/sections/section-0039.md) |
| [reda.007.001.01](../../../messages/reda.007.001.01/index.md) | P489 | [section-0044](documents/src-000377/sections/section-0044.md) |
| [reda.008.001.01](../../../messages/reda.008.001.01/index.md) | P384, P391, P420, P455 | [section-0040](documents/src-000377/sections/section-0040.md)<br>[section-0041](documents/src-000377/sections/section-0041.md)<br>[section-0042](documents/src-000377/sections/section-0042.md)<br>[section-0043](documents/src-000377/sections/section-0043.md) |
| [reda.009.001.01](../../../messages/reda.009.001.01/index.md) | P859 | [section-0056](documents/src-000377/sections/section-0056.md) |
| [reda.010.001.01](../../../messages/reda.010.001.01/index.md) | P744 | [section-0054](documents/src-000377/sections/section-0054.md) |
| [reda.012.001.01](../../../messages/reda.012.001.01/index.md) | P774 | [section-0055](documents/src-000377/sections/section-0055.md) |
| [reda.013.001.01](../../../messages/reda.013.001.01/index.md) | P622 | [section-0049](documents/src-000377/sections/section-0049.md) |
| [reda.029.001.01](../../../messages/reda.029.001.01/index.md) | P516, P523, P553, P588 | [section-0045](documents/src-000377/sections/section-0045.md)<br>[section-0046](documents/src-000377/sections/section-0046.md)<br>[section-0047](documents/src-000377/sections/section-0047.md)<br>[section-0048](documents/src-000377/sections/section-0048.md) |
| [reda.030.001.01](../../../messages/reda.030.001.01/index.md) | P637, P644, P674, P709 | [section-0050](documents/src-000377/sections/section-0050.md)<br>[section-0051](documents/src-000377/sections/section-0051.md)<br>[section-0052](documents/src-000377/sections/section-0052.md)<br>[section-0053](documents/src-000377/sections/section-0053.md) |
| [reda.033.001.01](../../../messages/reda.033.001.01/index.md) | P892 | [section-0057](documents/src-000377/sections/section-0057.md) |
| [reda.034.001.01](../../../messages/reda.034.001.01/index.md) | P915 | [section-0058](documents/src-000377/sections/section-0058.md) |



[src-000377](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`; Business Examples P318–P947. Source examples illustrate their stated conditions; they are not generalized to every use of the message. Namespace omissions in excerpts prevent claiming full schema validation.

<!-- SECREF-EXAMPLES-CHECK-START -->
## Literal example checks

All17 source Document excerpts were parsed without repair. Sixteen are well-formed XML fragments, one is not; none declares a namespace, so no complete XSD-validation pass is claimed. The completed Security Creation Status Advice at P398–P418 omits the opening SctyCreStsAdvc tag but closes it at P417. This is present in original OOXML and was directly confirmed in [Word page32](../../../../../../evidence/omitted/1701ff0a81903032030cf0c0.md). Source contents are preserved.

| Exact message | Source paragraph range | XML well-formedness | Namespace |
| --- | --- | --- | --- |
| reda.006.001.01 | P338–P383 | pass | not declared |
| reda.008.001.01 | P398–P418 | fail | not declared |
| reda.008.001.01 | P427–P453 | pass | not declared |
| reda.008.001.01 | P462–P488 | pass | not declared |
| reda.007.001.01 | P495–P515 | pass | not declared |
| reda.029.001.01 | P530–P551 | pass | not declared |
| reda.029.001.01 | P560–P586 | pass | not declared |
| reda.029.001.01 | P595–P621 | pass | not declared |
| reda.013.001.01 | P627–P636 | pass | not declared |
| reda.030.001.01 | P651–P672 | pass | not declared |
| reda.030.001.01 | P681–P707 | pass | not declared |
| reda.030.001.01 | P716–P742 | pass | not declared |
| reda.010.001.01 | P753–P772 | pass | not declared |
| reda.012.001.01 | P797–P857 | pass | not declared |
| reda.009.001.01 | P868–P890 | pass | not declared |
| reda.033.001.01 | P896–P913 | pass | not declared |
| reda.034.001.01 | P919–P945 | pass | not declared |


[Precise errors and excerpt hashes](../../../../../../tracking/reviews/securities-reference-examples.json) · [issue-000051](../../../../../../tracking/issues.md).

<!-- SECREF-EXAMPLES-CHECK-END -->
