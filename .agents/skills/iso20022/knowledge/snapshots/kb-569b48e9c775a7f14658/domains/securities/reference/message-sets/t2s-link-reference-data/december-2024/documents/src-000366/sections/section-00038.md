---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["5 reda.049.001.01 AccountLinkCreationRequestV01", "5.4 Message Building Blocks", "5.4.2 AccountLink <AcctLk>", "5.4.2.8 CashSettlementIndicator <CshSttlmInd>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 5.4.2.8 CashSettlementIndicator <CshSttlmInd>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
Definition: Specifies whether market infrastructure can use the securities, earmarked as collateral and
held on the securities account, for auto-collateralisation operations on the linked market infrastructure
dedicated cash account.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 77):
• Meaning When True: Yes
• Meaning When False: No
5.4.2.8  CashSettlementIndicator <CshSttlmInd>
Presence: [1..1]
Definition: Specifies whether market infrastructure can use the link between the securities account and
the market infrastructure dedicated cash account for the settlement of the cash leg of a settlement
instruction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 77):
• Meaning When True: Yes
• Meaning When False: No
5.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 67 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 67
   Envelope <Envlp> [1..1] (External Schema) 67
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 21 November 2024. reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities - Link Reference Data 40 December 2024
```

