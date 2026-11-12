---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.4 Message Building Blocks", "37.4.2 ReportOrError <RptOrErr>", "37.4.2.1 PartyReport <PtyRpt>"]
file_pages: [2083, 2084]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.4.2.1 PartyReport <PtyRpt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2083 to 2084.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2083

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           ValidFrom <VldFr> [1..1] DateTime 2095
           ValidTo <VldTo> [0..1] DateTime 2095
           Type <Tp> [1..1] Text 2095
Or}       BusinessError <BizErr> [1..*]  2095
         Error <Err> [1..1]  2095
{Or           Code <Cd> [1..1] CodeSet 2096
Or}           Proprietary <Prtry> [1..1] Text 2096
         Description <Desc> [0..1] Text 2096
Or}   OperationalError <OprlErr> [1..*]  2096
     Error <Err> [1..1]  2097
{Or       Code <Cd> [1..1] CodeSet 2097
Or}       Proprietary <Prtry> [1..1] Text 2097
     Description <Desc> [0..1] Text 2097
37.4.2.1  PartyReport <PtyRpt>
Presence: [1..*]
Definition: Report information about party reference data.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2083 August 2026
```

## File page 2084

```text
PartyReport <PtyRpt> contains the following PartyReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 2085
   PartyOrError <PtyOrErr> [1..1]  2085
{Or     SystemParty <SysPty> [1..1]  2087
       PartyIdentification <PtyId> [0..1]  2089
         Identification <Id> [1..1] ± 2089
         ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 2089
         ValidFrom <VldFr> [0..1] Date 2089
       Address <Adr> [0..1] ± 2089
       ContactDetails <CtctDtls> [0..*] ± 2090
       OpeningDate <OpngDt> [0..1] Date 2091
       ClosingDate <ClsgDt> [0..1] Date 2091
       Type <Tp> [0..1]  2091
{Or         Code <Cd> [1..1] CodeSet 2092
Or}         Proprietary <Prtry> [1..1] Text 2092
       TechnicalAddress <TechAdr> [0..*]  2092
{Or         BICFI <BICFI> [1..1] IdentifierSet C2 2092
Or}         TechnicalAddress <TechAdr> [1..1] Text 2092
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
         ValidFrom <VldFr> [1..1] DateTime 2095
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2084 August 2026
```

