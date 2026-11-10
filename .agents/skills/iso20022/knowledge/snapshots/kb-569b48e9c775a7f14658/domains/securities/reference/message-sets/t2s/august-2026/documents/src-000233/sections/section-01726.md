---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["65 reda.049.001.01 AccountLinkCreationRequestV01", "65.4 Message Building Blocks", "65.4.2 AccountLink <AcctLk>", "65.4.2.8 CashSettlementIndicator <CshSttlmInd>"]
file_pages: [2374]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 65.4.2.8 CashSettlementIndicator <CshSttlmInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2374 to 2374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2374

```text
Definition: Specifies whether market infrastructure can use the securities, earmarked as collateral and
held on the securities account, for auto-collateralisation operations on the linked market infrastructure
dedicated cash account.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
65.4.2.8  CashSettlementIndicator <CshSttlmInd>
Presence: [1..1]
Definition: Specifies whether market infrastructure can use the link between the securities account and
the market infrastructure dedicated cash account for the settlement of the cash leg of a settlement
instruction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
65.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities 2374 August 2026
```

