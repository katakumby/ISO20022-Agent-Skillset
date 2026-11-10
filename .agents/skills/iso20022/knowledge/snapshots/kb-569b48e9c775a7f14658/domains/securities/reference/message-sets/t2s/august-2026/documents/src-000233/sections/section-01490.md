---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["39 reda.019.001.01 SecuritiesAccountQueryV01", "39.3 Constraints"]
file_pages: [2108]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 39.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2108 to 2108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2108

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     AccountServicer <AcctSvcr> [0..1] Indicator 2116
     AccountType <AcctTp> [0..1] Indicator 2116
     OpeningDate <OpngDt> [0..1] Indicator 2116
     ClosingDate <ClsgDt> [0..1] Indicator 2116
     EndInvestorFlag <EndInvstrFlg> [0..1] Indicator 2117
     PricingScheme <PricgSchme> [0..1] Indicator 2117
   SupplementaryData <SplmtryData> [0..*] ± C3 2117
39.3 Constraints
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
39.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
39.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Point to point reference elements, as assigned by the instructing party, to unambiguously
identify the query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities 2108 August 2026
```

