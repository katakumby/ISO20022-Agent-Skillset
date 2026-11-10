---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.1 InterbankSettlementAmount <IntrBkSttlmAmt>"]
file_pages: [364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.1 InterbankSettlementAmount <IntrBkSttlmAmt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 364 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     DebtorAccount <DbtrAcct> [0..1] ± C22,
C21
550
     DebtorAgent <DbtrAgt> [0..1] ± 551
     DebtorAgentAccount <DbtrAgtAcct> [0..1] ± C22,
C21
551
     CreditorAgent <CdtrAgt> [0..1] ± 552
     CreditorAgentAccount <CdtrAgtAcct> [0..1] ± C22,
C21
553
     Creditor <Cdtr> [1..1] ± 554
     CreditorAccount <CdtrAcct> [0..1] ± C22,
C21
554
     UltimateCreditor <UltmtCdtr> [0..1] ± 555
     InstructionForCreditorAgent <InstrForCdtrAgt> [0..*] ± 556
     InstructionForNextAgent <InstrForNxtAgt> [0..*]  556
       Code <Cd> [0..1] CodeSet 557
       InstructionInformation <InstrInf> [0..1] Text 557
     Purpose <Purp> [0..1] ± 557
     RemittanceInformation <RmtInf> [0..1] ± 557
     UnderlyingAllocation <UndrlygAllcn> [0..*]  C80 558
       Amount <Amt> [1..1] Amount C2, C12 558
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 559
       Account <Acct> [1..1] ± C22,
C21
559
       Purpose <Purp> [1..1] ± 559
       Reference <Ref> [1..1] Text 560
       RelatedReferences <RltdRefs> [0..*] ± 560
Constraints
• UnderlyingCustomerCreditTransferRule
The UnderlyingCustomerCreditTransfer element can only be present if present in the original
transaction being returned.
• UnderlyingFinancialInstitutionCreditTransferRule
The UnderlyingFinancialInstitutionCreditTransfer element can only be present if present in the
original transaction being returned.
4.4.3.27.1  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
364 March 2026
```

