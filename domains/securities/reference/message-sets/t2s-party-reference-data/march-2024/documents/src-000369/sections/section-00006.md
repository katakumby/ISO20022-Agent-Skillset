---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 reda.014.001.02 PartyCreationRequestV02", "2.3 Constraints"]
file_pages: [8, 9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 2.3 Constraints

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 8 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       ValidFrom <VldFr> [1..1] DateTime 16
       ValidTo <VldTo> [0..1] DateTime 16
       Type <Tp> [1..1] Text 16
   SupplementaryData <SplmtryData> [0..*] ± C4 16
2.3 Constraints
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
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 161 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 161
   CreationDateTime <CreDtTm> [0..1] DateTime 161
2.4.2 Party <Pty>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.014.001.02 PartyCreationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
8 March 2024
```

## File page 9

```text
Definition: Specifies the details of the party to be created in the system.
Party <Pty> contains the following SystemParty7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1]  10
     Identification <Id> [1..1] ± 10
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 10
     ValidFrom <VldFr> [0..1] Date 10
   Address <Adr> [0..*] ± 10
   ContactDetails <CtctDtls> [0..*] ± 11
   OpeningDate <OpngDt> [0..1] Date 12
   ClosingDate <ClsgDt> [0..1] Date 12
   Type <Tp> [1..1]  12
{Or     Code <Cd> [1..1] CodeSet 13
Or}     Proprietary <Prtry> [1..1] Text 13
   TechnicalAddress <TechAdr> [0..*]  13
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 13
Or}     TechnicalAddress <TechAdr> [1..1] Text 13
   MarketSpecificAttribute <MktSpcfcAttr> [0..*]  14
     Name <Nm> [1..1] Text 14
     Value <Val> [1..1] Text 14
   Name <Nm> [0..1]  14
     ValidFrom <VldFr> [0..1] Date 14
     Name <Nm> [1..1] Text 14
     ShortName <ShrtNm> [0..1] Text 15
   ResidenceType <ResTp> [0..1] CodeSet 15
   LockStatus <LckSts> [0..1]  15
     ValidFrom <VldFr> [0..1] Date 15
     Status <Sts> [1..1] CodeSet 15
     LockReason <LckRsn> [0..*] Text 16
   Restriction <Rstrctn> [0..*]  16
     ValidFrom <VldFr> [1..1] DateTime 16
     ValidTo <VldTo> [0..1] DateTime 16
     Type <Tp> [1..1] Text 16
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.014.001.02 PartyCreationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
9 March 2024
```

