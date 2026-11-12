---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["34 reda.014.001.02 PartyCreationRequestV02", "34.3 Constraints"]
file_pages: [2045, 2046]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02"]
---

# 34.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2045 to 2046.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2045

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       ValidFrom <VldFr> [1..1] DateTime 2053
       ValidTo <VldTo> [0..1] DateTime 2053
       Type <Tp> [1..1] Text 2053
   SupplementaryData <SplmtryData> [0..*] ± C4 2053
34.3 Constraints
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
34.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
34.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
34.4.2 Party <Pty>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.014.001.02 PartyCreationRequestV02
Target2-Securities 2045 August 2026
```

## File page 2046

```text
Definition: Specifies the details of the party to be created in the system.
Party <Pty> contains the following SystemParty7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1]  2047
     Identification <Id> [1..1] ± 2047
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2047
     ValidFrom <VldFr> [0..1] Date 2047
   Address <Adr> [0..*] ± 2047
   ContactDetails <CtctDtls> [0..*] ± 2048
   OpeningDate <OpngDt> [0..1] Date 2049
   ClosingDate <ClsgDt> [0..1] Date 2049
   Type <Tp> [1..1]  2049
{Or     Code <Cd> [1..1] CodeSet 2050
Or}     Proprietary <Prtry> [1..1] Text 2050
   TechnicalAddress <TechAdr> [0..*]  2050
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 2050
Or}     TechnicalAddress <TechAdr> [1..1] Text 2050
   MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2051
     Name <Nm> [1..1] Text 2051
     Value <Val> [1..1] Text 2051
   Name <Nm> [0..1]  2051
     ValidFrom <VldFr> [0..1] Date 2051
     Name <Nm> [1..1] Text 2051
     ShortName <ShrtNm> [0..1] Text 2052
   ResidenceType <ResTp> [0..1] CodeSet 2052
   LockStatus <LckSts> [0..1]  2052
     ValidFrom <VldFr> [0..1] Date 2052
     Status <Sts> [1..1] CodeSet 2052
     LockReason <LckRsn> [0..*] Text 2053
   Restriction <Rstrctn> [0..*]  2053
     ValidFrom <VldFr> [1..1] DateTime 2053
     ValidTo <VldTo> [0..1] DateTime 2053
     Type <Tp> [1..1] Text 2053
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.014.001.02 PartyCreationRequestV02
Target2-Securities 2046 August 2026
```

