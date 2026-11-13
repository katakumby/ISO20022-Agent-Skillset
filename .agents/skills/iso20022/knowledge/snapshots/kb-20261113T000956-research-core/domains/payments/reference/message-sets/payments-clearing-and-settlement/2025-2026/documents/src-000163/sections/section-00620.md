---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks"]
file_pages: [848, 849]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
preceding_topic_continuations: [{"constraint_ids": ["C72", "C73", "C74", "C75", "C76", "C77", "C78", "C79"], "until_heading": "7.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 848, "topic": "7.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00619.md"}]
---

# 7.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 848 to 849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 848, C72–C79 before **7.4 Message Building Blocks** continue [7.3 Constraints](section-00619.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 848

```text
    /CreditTransferTransactionInformation[*]/InterbankSettlementDate Must be 
present
This constraint is defined at the MessageDefinition level.
C72 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C73 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C74 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C75 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
C76 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
C77 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
C78 UnderlyingAllocationGuideline
UnderlyingAllocation may only be present if bilaterally agreed.
C79 UnderlyingCustomerAndFinancialInstitutionCreditTransferRule
UnderlyingFinancialInstitutionCreditTransfer or UnderlyingCustomerCreditTransfer must be
absent.
Both may be absent.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the message.
Impacted by: C67 "TotalInterbankSettlementAmountAndDateRule"
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
848 March 2026
```

## File page 849

```text
GroupHeader <GrpHdr> contains the following GroupHeader131 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 850
   CreationDateTime <CreDtTm> [1..1] DateTime 850
   ExpiryDateTime <XpryDtTm> [0..1] DateTime 850
   BatchBooking <BtchBookg> [0..1] Indicator 850
   NumberOfTransactions <NbOfTxs> [1..1] Text 850
   ControlSum <CtrlSum> [0..1] Quantity 851
   TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C8 851
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 851
   SettlementInformation <SttlmInf> [1..1]  C18,
C20,
C59,
C60,
C61,
C62,
C65,
C66
851
     SettlementMethod <SttlmMtd> [1..1] CodeSet 853
     SettlementAccount <SttlmAcct> [0..1] ± C16,
C15
854
     ClearingSystem <ClrSys> [0..1]  854
{Or       Code <Cd> [1..1] CodeSet 855
Or}       Proprietary <Prtry> [1..1] Text 855
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 855
     InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C16,
C15
856
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 856
     InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
857
     ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 858
     ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C16,
C15
858
   PaymentTypeInformation <PmtTpInf> [0..1] ± 859
   InstructingAgent <InstgAgt> [0..1] ± 860
   InstructedAgent <InstdAgt> [0..1] ± 861
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
849 March 2026
```

