---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.21 ReturnInformation <RtrInf>", "2.4.2.15.18.2.21.1 OriginalBankTransactionCode <OrgnlBkTxCd>"]
file_pages: [225]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.21.1 OriginalBankTransactionCode <OrgnlBkTxCd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 225 to 225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 225

```text
ReturnInformation <RtrInf> contains the following PaymentReturnReason8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalBankTransactionCode <OrgnlBkTxCd> [0..1] ± C11,
C14
225
   Originator <Orgtr> [0..1] ± 226
   Reason <Rsn> [0..1]  227
{Or     Code <Cd> [1..1] CodeSet 228
Or}     Proprietary <Prtry> [1..1] Text 228
   AdditionalInformation <AddtlInf> [0..*] Text 228
Constraints
• ReturnReasonRule
If Reason/Code is equal to NARR, then AdditionalInformation must be present.
On Condition
    /Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
 And    /Reason is present
 And    /Reason/Code is present
Following Must be True
    /AdditionalInformation[*] Must be present
2.4.2.15.18.2.21.1  OriginalBankTransactionCode <OrgnlBkTxCd>
Presence: [0..1]
Definition: Bank transaction code included in the original entry for the transaction.
Impacted by: C11 "DomainOrProprietaryRule", C14 "FamilyAndSubFamilyRule"
OriginalBankTransactionCode <OrgnlBkTxCd> contains the following elements (see
"BankTransactionCodeStructure4" on page 821 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Domain <Domn> [0..1] ± 821
   Proprietary <Prtry> [0..1]  821
     Code <Cd> [1..1] Text 822
     Issuer <Issr> [0..1] Text 822
Constraints
• DomainOrProprietaryRule
Either Proprietary or Domain or both must be present.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
225 March 2026
```

