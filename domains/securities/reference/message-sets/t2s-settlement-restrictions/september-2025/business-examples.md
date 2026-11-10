---
template: false
document_kind: "business-examples-index"
review_status: "needs-review"
source_ids: ["src-000380"]
domain: "securities"
message_sets: ["t2s-settlement-restrictions"]
message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.031.001.01", "semt.032.001.01", "semt.033.001.01", "semt.034.001.01"]
source_locations: [{"source_id": "src-000380", "locator": "Business Examples P311–P1422"}]
limitations: ["Source XML excerpts are parsed literally without repair. Schema validation is separate and not claimed by this well-formedness check.", "P312 explicitly says the instances are embedded in BAH but prints only pure business-message content. The excerpts omit Document and namespace wrappers; none is manufactured."]
source_editions: ["september-2025"]
---

# Settlement Restrictions business examples

[src-000380](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; P311–P1422. P312 states that the examples show only pure business-message content although the XML instances are embedded in BAH. The source conditions, literal values and complete payload excerpts are retained in focused source sections. No Document wrapper or namespace is added.

| Exact definition via companion Part2 | Source excerpt | XML well-formedness | Namespace declared |
| --- | --- | --- | --- |
| semt.028.001.01 | P318–P343 | pass | False |
| semt.029.001.01 | P350–P735 | pass | False |
| semt.030.001.01 | P741–P756 | pass | False |
| semt.031.001.01 | P764–P1003 | pass | False |
| semt.032.001.01 | P1011–P1029 | pass | False |
| semt.033.001.01 | P1036–P1216 | pass | False |
| semt.034.001.01 | P1224–P1421 | pass | False |



[Exact errors and source text hashes](../../../../../../tracking/reviews/settlement-restrictions-examples.json)

- [section-0035](documents/src-000380/sections/section-0035.md)
- [section-0036](documents/src-000380/sections/section-0036.md)
- [section-0037](documents/src-000380/sections/section-0037.md)
- [section-0038](documents/src-000380/sections/section-0038.md)
- [section-0039](documents/src-000380/sections/section-0039.md)
- [section-0040](documents/src-000380/sections/section-0040.md)
- [section-0041](documents/src-000380/sections/section-0041.md)
