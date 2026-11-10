---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.3 Constraints"]
file_pages: [2296]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.3 Constraints

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2296 to 2296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2296

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         FromToDate <FrToDt> [1..1] ± 2332
Or}         Date <Dt> [1..1] Date 2332
       PartyIdentification <PtyId> [1..1] ± 2332
Or}     OperationalError <OprlErr> [1..*]  2333
       Error <Err> [1..1]  2333
{Or         Code <Cd> [1..1] CodeSet 2333
Or}         Proprietary <Prtry> [1..1] Text 2333
       Description <Desc> [0..1] Text 2333
   SupplementaryData <SplmtryData> [0..*] ± C4 2334
60.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
60.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
60.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2296 August 2026
```

