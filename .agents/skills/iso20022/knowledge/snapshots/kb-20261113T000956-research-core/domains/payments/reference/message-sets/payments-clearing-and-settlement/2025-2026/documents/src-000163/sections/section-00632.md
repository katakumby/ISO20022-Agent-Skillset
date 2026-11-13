---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [871, 872]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# Continuation at file page 871

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 871 to 872.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 871

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     CreditorAgent <CdtrAgt> [0..1] ± 1005
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C16,
C15
1006
     Creditor <Cdtr> [1..1] ± 1007
     CreditorAccount <CdtrAcct> [0..1] ± C16,
C15
1007
     UltimateCreditor <UltmtCdtr> [0..1] ± 1008
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 1009
     InstructionForNextAgent <InstrForNxtAgt> [0..*]  1009
       Code <Cd> [0..1] CodeSet 1010
       InstructionInformation <InstrInf> [0..1] Text 1010
     Purpose <Purp> [0..1] ± 1010
     RegulatoryReporting <RgltryRptg> [0..10] ± 1010
     RemittanceInformation <RmtInf> [0..1] ± 1011
     UnderlyingAllocation <UndrlygAllcn> [0..*]  C78 1011
       Amount <Amt> [1..1] Amount C2, C9 1012
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1012
       Account <Acct> [1..1] ± C16,
C15
1013
       Purpose <Purp> [1..1] ± 1013
       Reference <Ref> [1..1] Text 1013
       RelatedReferences <RltdRefs> [0..*] ± 1014
   SupplementaryData <SplmtryData> [0..*] ± C64 1014
Constraints
• CreditorAgentAccountRule
If CreditorAgentAccount is present, then CreditorAgent must be present.
On Condition
    /CreditorAgent is absent
Following Must be True
    /CreditorAgentAccount Must be absent
• DebtorAgentAccountRule
If DebtorAgentAccount is present, then DebtorAgent must be present.
On Condition
    /DebtorAgent is absent
Following Must be True
    /DebtorAgentAccount Must be absent
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
871 March 2026
```

## File page 872

```text
• IntermediaryAgent1AccountRule
If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent1 is absent
Following Must be True
    /IntermediaryAgent1Account Must be absent
• IntermediaryAgent1Rule
If IntermediaryAgent1 is present, then CreditorAgent must be present.
On Condition
    /IntermediaryAgent1 is present
Following Must be True
    /CreditorAgent Must be present
• IntermediaryAgent2AccountRule
If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent2 is absent
Following Must be True
    /IntermediaryAgent2Account Must be absent
• IntermediaryAgent2Rule
If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.
On Condition
    /IntermediaryAgent2 is present
Following Must be True
    /IntermediaryAgent1 Must be present
• IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
On Condition
    /IntermediaryAgent3 is absent
Following Must be True
    /IntermediaryAgent3Account Must be absent
• IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent3 is present
Following Must be True
    /IntermediaryAgent2 Must be present
• PreviousInstructingAgent1AccountRule
If PreviousInstructingAgent1Account is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent1 is absent
Following Must be True
    /PreviousInstructingAgent1Account Must be absent
• PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the DebtorAgent
in the payment chain.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
872 March 2026
```

