---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["21 camt.023.001.07 BackupPaymentV07", "21.2 Structure"]
file_pages: [579]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.023.001.07"]
---

# 21.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 579 to 579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 579

```text
21.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BckpPmt> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 580
   OriginalMessageIdentification <OrgnlMsgId> [0..1] ± 580
   InstructionInformation <InstrInf> [0..1]  581
     RequestedExecutionDateTime <ReqdExctnDtTm> [0..1] DateTime 581
     PaymentType <PmtTp> [0..1]  581
{Or       Code <Cd> [1..1] CodeSet 581
Or}       Proprietary <Prtry> [1..1] Text 583
   TransferredAmount <TrfdAmt> [1..1] ± 583
   Creditor <Cdtr> [1..1]  584
     SystemIdentification <SysId> [0..1] ± 584
     MemberIdentification <MmbId> [1..1]  584
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 584
Or       ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 585
Or}       Other <Othr> [1..1] ± 585
   CreditorAgent <CdtrAgt> [0..1]  585
     SystemIdentification <SysId> [0..1] ± 586
     MemberIdentification <MmbId> [1..1]  586
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 586
Or       ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 587
Or}       Other <Othr> [1..1] ± 587
   DebtorAgent <DbtrAgt> [0..1]  587
     SystemIdentification <SysId> [0..1] ± 588
     MemberIdentification <MmbId> [1..1]  588
{Or       BICFI <BICFI> [1..1] IdentifierSet C2 588
Or       ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 589
Or}       Other <Othr> [1..1] ± 589
   SupplementaryData <SplmtryData> [0..*] ± C5 589
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 579 February 2025
```

