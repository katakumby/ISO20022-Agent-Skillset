---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.4 Message Building Blocks", "8.4.2 PartyActivity <PtyActvty>", "8.4.2.2 Change <Chng>", "8.4.2.2.1 PartyIdentification <PtyId>"]
file_pages: [89, 90, 91]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.4.2.2.1 PartyIdentification <PtyId>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 89 to 91.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ValidUntil <VldUntil> [0..1] DateTime 107
       New <New> [1..1]  107
         RestrictionType <RstrctnTp> [1..1]  108
{Or           Code <Cd> [1..1] Text 108
Or}           Proprietary <Prtry> [1..1] ± 108
         ValidFrom <VldFr> [1..1] DateTime 108
         ValidUntil <VldUntil> [0..1] DateTime 109
Or}     Other <Othr> [1..*]  109
       FieldName <FldNm> [1..1] Text 109
       OldFieldValue <OdFldVal> [1..1] Text 109
       NewFieldValue <NewFldVal> [1..1] Text 109
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 109
8.4.2.2.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Identifies the party for which the changes are listed in the advice.
PartyIdentification <PtyId> contains the following elements (see "SystemPartyIdentification8" on
page 170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 170
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 170
8.4.2.2.2  Record <Rcrd>
Presence: [1..*]
Definition: Provides the party data record for which details of the change are provided.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
89 March 2024
```

## File page 90

```text
Record <Rcrd> contains one of the following UpdateLogPartyRecord2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Address <Adr> [1..1]  92
     Old <Od> [1..1] ± 92
     New <New> [1..1] ± 93
Or   ContactDetails <CtctDtls> [1..1]  94
     Old <Od> [1..1] ± 94
     New <New> [1..1] ± 95
Or   OpeningDate <OpngDt> [1..1]  96
     Old <Od> [1..1] Date 96
     New <New> [1..1] Date 96
Or   ClosingDate <ClsgDt> [1..1]  97
     Old <Od> [1..1] Date 97
     New <New> [1..1] Date 97
Or   Type <Tp> [1..1]  97
     Old <Od> [1..1]  97
{Or       Code <Cd> [1..1] CodeSet 98
Or}       Proprietary <Prtry> [1..1] Text 98
     New <New> [1..1]  98
{Or       Code <Cd> [1..1] CodeSet 98
Or}       Proprietary <Prtry> [1..1] Text 98
Or   TechnicalAddress <TechAdr> [1..1]  98
     Old <Od> [1..1]  99
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 99
Or}       TechnicalAddress <TechAdr> [1..1] Text 99
     New <New> [1..1]  99
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 100
Or}       TechnicalAddress <TechAdr> [1..1] Text 100
Or   MarketSpecificAttribute <MktSpcfcAttr> [1..1]  100
     Old <Od> [1..1]  100
       Name <Nm> [1..1] Text 101
       Value <Val> [1..1] Text 101
     New <New> [1..1]  101
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
90 March 2024
```

## File page 91

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Name <Nm> [1..1] Text 101
       Value <Val> [1..1] Text 101
Or   Name <Nm> [1..1]  101
     Old <Od> [1..1]  102
       ValidFrom <VldFr> [0..1] Date 102
       Name <Nm> [1..1] Text 102
       ShortName <ShrtNm> [0..1] Text 102
     New <New> [1..1]  102
       ValidFrom <VldFr> [0..1] Date 103
       Name <Nm> [1..1] Text 103
       ShortName <ShrtNm> [0..1] Text 103
Or   ResidenceType <ResTp> [1..1]  103
     Old <Od> [1..1] CodeSet 103
     New <New> [1..1] CodeSet 104
Or   LockStatus <LckSts> [1..1]  104
     Old <Od> [1..1]  104
       ValidFrom <VldFr> [0..1] Date 105
       Status <Sts> [1..1] CodeSet 105
       LockReason <LckRsn> [0..*] Text 105
     New <New> [1..1]  105
       ValidFrom <VldFr> [0..1] Date 105
       Status <Sts> [1..1] CodeSet 105
       LockReason <LckRsn> [0..*] Text 106
Or   Restriction <Rstrctn> [1..1]  106
     Old <Od> [1..1]  106
       RestrictionType <RstrctnTp> [1..1]  107
{Or         Code <Cd> [1..1] Text 107
Or}         Proprietary <Prtry> [1..1] ± 107
       ValidFrom <VldFr> [1..1] DateTime 107
       ValidUntil <VldUntil> [0..1] DateTime 107
     New <New> [1..1]  107
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
91 March 2024
```

