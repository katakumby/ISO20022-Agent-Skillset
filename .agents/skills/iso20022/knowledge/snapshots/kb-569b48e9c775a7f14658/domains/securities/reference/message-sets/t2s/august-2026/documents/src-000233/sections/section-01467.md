---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.4 Message Building Blocks"]
file_pages: [2081, 2082]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2081 to 2082.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2081

```text
37.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
37.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Point to point reference elements, as assigned by the instructing party, to unambiguously
identify the report message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader3" on page 2995 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2995
   CreationDateTime <CreDtTm> [0..1] DateTime 2995
   RequestType <ReqTp> [0..1]  2995
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 2995
Or     Enquiry <Enqry> [1..1] CodeSet 2996
Or}     Proprietary <Prtry> [1..1] ± 2996
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 2996
   QueryName <QryNm> [0..1] Text 2997
37.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Provides information on report or error resulting from the originating query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2081 August 2026
```

## File page 2082

```text
ReportOrError <RptOrErr> contains one of the following PartyOrOperationalError4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PartyReport <PtyRpt> [1..*]  2083
     PartyIdentification <PtyId> [1..1] ± 2085
     PartyOrError <PtyOrErr> [1..1]  2085
{Or       SystemParty <SysPty> [1..1]  2087
         PartyIdentification <PtyId> [0..1]  2089
           Identification <Id> [1..1] ± 2089
           ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2089
           ValidFrom <VldFr> [0..1] Date 2089
         Address <Adr> [0..1] ± 2089
         ContactDetails <CtctDtls> [0..*] ± 2090
         OpeningDate <OpngDt> [0..1] Date 2091
         ClosingDate <ClsgDt> [0..1] Date 2091
         Type <Tp> [0..1]  2091
{Or           Code <Cd> [1..1] CodeSet 2092
Or}           Proprietary <Prtry> [1..1] Text 2092
         TechnicalAddress <TechAdr> [0..*]  2092
{Or           BICFI <BICFI> [1..1] IdentifierSet C2 2092
Or}           TechnicalAddress <TechAdr> [1..1] Text 2092
         MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2093
           Name <Nm> [1..1] Text 2093
           Value <Val> [1..1] Text 2093
         Name <Nm> [0..1]  2093
           ValidFrom <VldFr> [0..1] Date 2093
           Name <Nm> [1..1] Text 2093
           ShortName <ShrtNm> [0..1] Text 2093
         ResidenceType <ResTp> [0..1] CodeSet 2094
         LockStatus <LckSts> [0..1]  2094
           ValidFrom <VldFr> [0..1] Date 2094
           Status <Sts> [1..1] CodeSet 2094
           LockReason <LckRsn> [0..*] Text 2094
         Restriction <Rstrctn> [0..*]  2095
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2082 August 2026
```

