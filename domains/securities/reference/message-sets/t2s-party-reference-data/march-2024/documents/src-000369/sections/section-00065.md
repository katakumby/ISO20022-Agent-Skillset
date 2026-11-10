---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["7 reda.031.001.01 PartyDeletionRequestV01", "7.3 Constraints"]
file_pages: [77, 78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.031.001.01"]
---

# 7.3 Constraints

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 77 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
7.3 Constraints
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
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 161 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 161
   CreationDateTime <CreDtTm> [0..1] DateTime 161
7.4.2 SystemPartyIdentification <SysPtyId>
Presence: [1..1]
Definition: Unique identification, as assigned by the executing system, to unambiguously identify the
party to be deleted.
SystemPartyIdentification <SysPtyId> contains the following elements (see
"SystemPartyIdentification8" on page 170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 170
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 170
7.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.031.001.01 PartyDeletionRequestV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
77 March 2024
```

## File page 78

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 163 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 163
   Envelope <Envlp> [1..1] (External Schema) 163
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.031.001.01 PartyDeletionRequestV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
78 March 2024
```

