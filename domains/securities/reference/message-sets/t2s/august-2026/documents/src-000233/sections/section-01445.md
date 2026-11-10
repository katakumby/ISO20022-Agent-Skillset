---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.3 Constraints"]
file_pages: [2058, 2059]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.3 Constraints

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2058 to 2059.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2058

```text
35.3 Constraints
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
35.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
35.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Point to point reference elements, as assigned by the instructing party, to unambiguously
identify the query message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader2" on page 3007 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3007
   CreationDateTime <CreDtTm> [0..1] DateTime 3008
   RequestType <ReqTp> [0..1]  3008
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 3008
Or     Enquiry <Enqry> [1..1] CodeSet 3008
Or}     Proprietary <Prtry> [1..1] ± 3009
35.4.2 SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to query the party reference data by the executing system.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2058 August 2026
```

## File page 2059

```text
SearchCriteria <SchCrit> contains the following PartyDataSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningDate <OpngDt> [0..1]  2060
{Or     FromDate <FrDt> [1..1] Date 2060
Or     ToDate <ToDt> [1..1] Date 2060
Or     FromToDate <FrToDt> [1..1] ± 2060
Or     EqualDate <EQDt> [1..1] Date 2061
Or}     NotEqualDate <NEQDt> [1..1] Date 2061
   ClosingDate <ClsgDt> [0..1]  2061
{Or     FromDate <FrDt> [1..1] Date 2061
Or     ToDate <ToDt> [1..1] Date 2061
Or     FromToDate <FrToDt> [1..1] ± 2061
Or     EqualDate <EQDt> [1..1] Date 2062
Or}     NotEqualDate <NEQDt> [1..1] Date 2062
   Type <Tp> [0..1]  2062
{Or     Code <Cd> [1..1] CodeSet 2062
Or}     Proprietary <Prtry> [1..1] Text 2062
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2062
   PartyIdentification <PtyId> [0..1] ± 2063
   RestrictionIdentification <RstrctnId> [0..1] Text 2063
   RestrictionIssueDate <RstrctnIsseDt> [0..1]  2063
{Or     DateTime <DtTm> [1..1]  2064
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2064
Or       ToDateTime <ToDtTm> [1..1] DateTime 2064
Or       FromToDateTime <FrToDtTm> [1..1] ± 2065
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2065
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2065
Or}     Date <Dt> [1..1]  2065
{Or       FromDate <FrDt> [1..1] Date 2065
Or       ToDate <ToDt> [1..1] Date 2065
Or       FromToDate <FrToDt> [1..1] ± 2066
Or       EqualDate <EQDt> [1..1] Date 2066
Or}       NotEqualDate <NEQDt> [1..1] Date 2066
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2059 August 2026
```

