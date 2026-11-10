---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.1 SystemPartyDate <SysPtyDt>"]
file_pages: [67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3.2.1 SystemPartyDate <SysPtyDt>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 67 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 67

```text
RequestedModification <ReqdMod> contains one of the following
SystemPartyModification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SystemPartyDate <SysPtyDt> [1..1]  67
     OpeningDate <OpngDt> [0..1] Date 68
     ClosingDate <ClsgDt> [0..1] Date 68
Or   PartyIdentification <PtyId> [1..1]  68
     ValidFrom <VldFr> [0..1] Date 68
     Identification <Id> [0..1] ± 68
Or   PartyName <PtyNm> [1..1]  69
     ValidFrom <VldFr> [0..1] Date 69
     Name <Nm> [0..1] Text 69
     ShortName <ShrtNm> [0..1] Text 69
Or   ContactDetails <CtctDtls> [1..1] ± 69
Or   TechnicalAddress <TechAdr> [1..1]  70
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 70
Or}     TechnicalAddress <TechAdr> [1..1] Text 71
Or   PartyAddress <PtyAdr> [1..1] ± 71
Or   ResidenceType <ResTp> [1..1] CodeSet 72
Or   LockStatus <LckSts> [1..1]  73
     ValidFrom <VldFr> [0..1] Date 73
     Status <Sts> [1..1] CodeSet 73
     LockReason <LckRsn> [0..*] Text 73
Or   SystemRestriction <SysRstrctn> [1..1]  73
     ValidFrom <VldFr> [1..1] DateTime 74
     ValidTo <VldTo> [0..1] DateTime 74
     Type <Tp> [1..1] Text 74
Or}   MarketSpecificAttribute <MktSpcfcAttr> [1..1]  74
     Name <Nm> [1..1] Text 74
     Value <Val> [1..1] Text 74
6.4.3.2.1  SystemPartyDate <SysPtyDt>
Presence: [1..1]
Definition: Specifies the opening and closing dates, as assigned by the system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
67 March 2024
```

