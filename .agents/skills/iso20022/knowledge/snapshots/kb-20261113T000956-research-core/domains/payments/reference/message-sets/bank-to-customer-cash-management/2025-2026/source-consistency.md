---
template: false
document_kind: "source-limitation"
manual_curated: true
review_status: "needs-review"
domain: "payments"
title: "Bank-to-customer source consistency limitations"
source_ids: ["src-000004"]
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
source_locations: [{"source_id": "src-000004", "locator": "T14-T15 Word13-15; Business Examples T18-T21/P159-P551 Word23-40"}]
issue_ids: ["issue-000060"]
limitations: ["Source responsibility, label, date, value, tag and request-target discrepancies are retained without inferred corrections."]
source_editions: ["March 2026"]
---

# Bank-to-customer source consistency limitations

[src-000004](../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md); all claims below visually compared with the complete Word rendering.

| Source locator | Conflicting evidence retained |
| --- | --- |
| T14 rows3/5; P116; Word13-14 | Initiators Cash Position Evaluation Position versus CashPositionEvaluationSystem lane and other System table rows. Both scoped source labels retained; no alias equivalence asserted. |
| T15 row5; P118; Word14-15 | Receive notification description and AccountOwner lane say the owner receives; Initiator cell says Account Servicer. All notifications are explicitly optional under the service agreement. |
| P159/P269/P445; Word23/28/35 versus T18-T20/XML P165/P275/P451 | Narratives give 18 October2010; business-data and payload dates give2015. |
| T18 rows41/66 Word24-25 versus P221/P258 Word26-27 | PaymentInformationId FINP-0055/001 versus FINP-0055-001; exchange rate0.1085 versus0.185. |
| T19 row46/50 Word29 versus P342/P348 Word32 | AccountServicerReference AAAASESS-FP-CN-98765/01 versus AAAASESS-FP-CN_98765/01; first credit SubFamilyCode DMCT versus BOOK. |
| P517/T21 rows4/6; Word38 versus P523/P526 Word39 | Description requests BankToCustomerStatement, while table requests camt.052.001.09 and XML requests camt.052.001.08. Table time10:05:00 differs from XML17:15:00. None is silently updated to .14 or camt.053. |
| T18-T21 tag cells; Word23-39 | Table XML-tag labels have spelling/case/structure differences from payload and schema, including missing angle bracket and nested code containers. Source table values remain literal evidence. |
| T20 Word36; P489/P491/P492 Word37 | Bank transaction codes PAYM / 0001 / 0005 are literal source example values with leading zeros preserved. Exact XSD only checks external-code type structure, not membership in a separately versioned current publication. No membership claim is inferred. |



All four original fragments parse as XML. All four derived copies pass their exact supplied XSD after adding only the exact namespace and Document envelope. That structural result does not resolve the business or example contradictions above. Every XML source paragraph is independently corroborated by the rendered Word PDF with zero unmatched paragraphs.
