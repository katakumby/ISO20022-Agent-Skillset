---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.2 Structure"]
file_pages: [80, 81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.2 Structure

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 80 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PtyActvtyAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 83
   PartyActivity <PtyActvty> [1..1]  83
     SystemDate <SysDt> [1..1] Date 86
     Change <Chng> [0..*]  86
       PartyIdentification <PtyId> [1..1] ± 89
       Record <Rcrd> [1..*]  89
{Or         Address <Adr> [1..1]  92
           Old <Od> [1..1] ± 92
           New <New> [1..1] ± 93
Or         ContactDetails <CtctDtls> [1..1]  94
           Old <Od> [1..1] ± 94
           New <New> [1..1] ± 95
Or         OpeningDate <OpngDt> [1..1]  96
           Old <Od> [1..1] Date 96
           New <New> [1..1] Date 96
Or         ClosingDate <ClsgDt> [1..1]  97
           Old <Od> [1..1] Date 97
           New <New> [1..1] Date 97
Or         Type <Tp> [1..1]  97
           Old <Od> [1..1]  97
{Or             Code <Cd> [1..1] CodeSet 98
Or}             Proprietary <Prtry> [1..1] Text 98
           New <New> [1..1]  98
{Or             Code <Cd> [1..1] CodeSet 98
Or}             Proprietary <Prtry> [1..1] Text 98
Or         TechnicalAddress <TechAdr> [1..1]  98
           Old <Od> [1..1]  99
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 99
Or}             TechnicalAddress <TechAdr> [1..1] Text 99
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
80 March 2024
```

## File page 81

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           New <New> [1..1]  99
{Or             BICFI <BICFI> [1..1] IdentifierSet C2 100
Or}             TechnicalAddress <TechAdr> [1..1] Text 100
Or         MarketSpecificAttribute <MktSpcfcAttr> [1..1]  100
           Old <Od> [1..1]  100
             Name <Nm> [1..1] Text 101
             Value <Val> [1..1] Text 101
           New <New> [1..1]  101
             Name <Nm> [1..1] Text 101
             Value <Val> [1..1] Text 101
Or         Name <Nm> [1..1]  101
           Old <Od> [1..1]  102
             ValidFrom <VldFr> [0..1] Date 102
             Name <Nm> [1..1] Text 102
             ShortName <ShrtNm> [0..1] Text 102
           New <New> [1..1]  102
             ValidFrom <VldFr> [0..1] Date 103
             Name <Nm> [1..1] Text 103
             ShortName <ShrtNm> [0..1] Text 103
Or         ResidenceType <ResTp> [1..1]  103
           Old <Od> [1..1] CodeSet 103
           New <New> [1..1] CodeSet 104
Or         LockStatus <LckSts> [1..1]  104
           Old <Od> [1..1]  104
             ValidFrom <VldFr> [0..1] Date 105
             Status <Sts> [1..1] CodeSet 105
             LockReason <LckRsn> [0..*] Text 105
           New <New> [1..1]  105
             ValidFrom <VldFr> [0..1] Date 105
             Status <Sts> [1..1] CodeSet 105
             LockReason <LckRsn> [0..*] Text 106
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
81 March 2024
```

