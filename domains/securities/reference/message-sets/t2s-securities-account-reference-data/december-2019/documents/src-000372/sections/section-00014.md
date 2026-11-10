---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["3 reda.019.001.01 SecuritiesAccountQueryV01", "3.3 Constraints"]
file_pages: [16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 3.3 Constraints

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 16 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 16

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     AccountServicer <AcctSvcr> [0..1] Indicator 24
     AccountType <AcctTp> [0..1] Indicator 24
     OpeningDate <OpngDt> [0..1] Indicator 24
     ClosingDate <ClsgDt> [0..1] Indicator 24
     EndInvestorFlag <EndInvstrFlg> [0..1] Indicator 25
     PricingScheme <PricgSchme> [0..1] Indicator 25
   SupplementaryData <SplmtryData> [0..*] ± C3 25
3.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Point to point reference elements, as assigned by the instructing party, to unambiguously
identify the query message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 16 December 2019
```

