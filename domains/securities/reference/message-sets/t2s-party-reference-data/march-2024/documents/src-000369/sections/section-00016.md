---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.3 Constraints"]
file_pages: [21, 22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.3 Constraints

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 21 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
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
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader2" on page 166 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 166
   CreationDateTime <CreDtTm> [0..1] DateTime 166
   RequestType <ReqTp> [0..1]  166
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 167
Or     Enquiry <Enqry> [1..1] CodeSet 167
Or}     Proprietary <Prtry> [1..1] ± 167
3.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to query the party reference data by the executing system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
21 March 2024
```

## File page 22

```text
SearchCriteria <SchCrit> contains the following PartyDataSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningDate <OpngDt> [0..1]  23
{Or     FromDate <FrDt> [1..1] Date 23
Or     ToDate <ToDt> [1..1] Date 23
Or     FromToDate <FrToDt> [1..1] ± 23
Or     EqualDate <EQDt> [1..1] Date 24
Or}     NotEqualDate <NEQDt> [1..1] Date 24
   ClosingDate <ClsgDt> [0..1]  24
{Or     FromDate <FrDt> [1..1] Date 24
Or     ToDate <ToDt> [1..1] Date 24
Or     FromToDate <FrToDt> [1..1] ± 24
Or     EqualDate <EQDt> [1..1] Date 25
Or}     NotEqualDate <NEQDt> [1..1] Date 25
   Type <Tp> [0..1]  25
{Or     Code <Cd> [1..1] CodeSet 25
Or}     Proprietary <Prtry> [1..1] Text 25
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 25
   PartyIdentification <PtyId> [0..1] ± 26
   RestrictionIdentification <RstrctnId> [0..1] Text 26
   RestrictionIssueDate <RstrctnIsseDt> [0..1]  26
{Or     DateTime <DtTm> [1..1]  27
{Or       FromDateTime <FrDtTm> [1..1] DateTime 27
Or       ToDateTime <ToDtTm> [1..1] DateTime 27
Or       FromToDateTime <FrToDtTm> [1..1] ± 28
Or       EqualDateTime <EQDtTm> [1..1] DateTime 28
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 28
Or}     Date <Dt> [1..1]  28
{Or       FromDate <FrDt> [1..1] Date 28
Or       ToDate <ToDt> [1..1] Date 28
Or       FromToDate <FrToDt> [1..1] ± 29
Or       EqualDate <EQDt> [1..1] Date 29
Or}       NotEqualDate <NEQDt> [1..1] Date 29
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
22 March 2024
```

