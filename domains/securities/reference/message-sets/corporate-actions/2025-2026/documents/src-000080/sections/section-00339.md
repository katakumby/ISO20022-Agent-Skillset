---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.1 SecurityDetails <SctyDtls>", "7.4.13.22.1.11 NextCallableDate <NxtCllblDt>"]
file_pages: [462]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.1.11 NextCallableDate <NxtCllblDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 462 to 462.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 462

```text
Datatype: "ISODate" on page 1243
7.4.13.22.1.11  NextCallableDate <NxtCllblDt>
Presence: [0..1]
Definition: Date on which a financial instrument is called away/redeemed before its scheduled maturity.
Datatype: "ISODate" on page 1243
7.4.13.22.1.12  PutableDate <PutblDt>
Presence: [0..1]
Definition: Date on which a holder of a financial instrument has the right to request redemption of the
principal amount prior to its scheduled maturity date.
Datatype: "ISODate" on page 1243
7.4.13.22.1.13  DatedDate <DtdDt>
Presence: [0..1]
Definition: Date on which an interest bearing financial instrument begins to accrue interest.
Datatype: "ISODate" on page 1243
7.4.13.22.1.14  ConversionDate <ConvsDt>
Presence: [0..1]
Definition: Deadline by which a convertible security must be converted, according to the terms of the
issue.
Datatype: "ISODate" on page 1243
7.4.13.22.1.15  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) until the next redemption (factor) date.
PreviousFactor <PrvsFctr> contains one of the following elements (see "RateFormat12Choice" on
page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 971
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 971
7.4.13.22.1.16  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Factor used to calculate the value of the outstanding principal of the financial instrument (for
factored securities) that will applicable after the redemption (factor) date.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 462 February 2026
```

