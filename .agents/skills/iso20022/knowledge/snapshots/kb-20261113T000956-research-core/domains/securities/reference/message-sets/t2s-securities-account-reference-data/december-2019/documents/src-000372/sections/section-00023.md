---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["3 reda.019.001.01 SecuritiesAccountQueryV01", "3.4 Message Building Blocks", "3.4.3 ReturnCriteria <RtrCrit>", "3.4.3.8 EndInvestorFlag <EndInvstrFlg>"]
file_pages: [25]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 3.4.3.8 EndInvestorFlag <EndInvstrFlg>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 25 to 25.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 25

```text
3.4.3.8  EndInvestorFlag <EndInvstrFlg>
Presence: [0..1]
Definition: Specifies information to identify securities accounts where allocation instructions are posted.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 98):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.3.9  PricingScheme <PricgSchme>
Presence: [0..1]
Definition: Defines how the price is applied to the securities account.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 98):
• Meaning When True: Requested
• Meaning When False: Not Requested
3.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 84 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 84
   Envelope <Envlp> [1..1] (External Schema) 84
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 25 December 2019
```

