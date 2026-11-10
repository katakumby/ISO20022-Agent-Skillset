---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit", "PaymentReturn Initiated by Debtor Agent"]
content_origin: "source-transcription"
---

# PaymentReturn Initiated by Debtor Agent

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / PaymentReturn with Direct Debit / PaymentReturn Initiated by Debtor Agent.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P539** PaymentReturn Initiated by Debtor Agent

**P540** If booking of the original instruction on the creditor account has already taken place, the return of funds will be notified to the creditor through return information included in the BankToCustomerNotification message (notification) and/or the BankToCustomerAccountReport or the BankToCustomerStatement message (Statement).

[fig-0041 - original figure evidence](../diagrams/fig-0041.md)

**P542** The creditor initiates the direct debit (for example by sending) the CustomerDirectDebitInitiation message to its agent (the creditor agent).

**P543** The creditor agent confirms the processability of the instruction by sending for example a positive CustomerPaymentStatusReport to the creditor.

**P544** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P545** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P546** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, together with potentially the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

**P547** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent.

**P548** If the debtor agent is unable to make the collection from the debtor Account for one or several reasons (insufficient funds, customer deceased...), It will initiate a PaymentReturn message, and route it through the clearing and settlement agent to the creditor agent, giving the reason for the Return.

**P549** The clearing and settlement agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**P550** The clearing and settlement agent forwards the PaymentReturn message to the creditor agent.

**P551** If clearing and settlement is carried out by two parties,  the clearing agent prepares the (returned) payment information for the settlement agent (the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date) in accordance with the agreed and published settlement cycle. The settlement agent performs the transfer of cash from the credit party to the debit party (in accordance with the agreed published settlement cycle). (Out of scope and not illustrated).

**P552** The creditor agent may, optionally, confirm receipt of the PaymentReturn message to the clearing agent. Depending on agreements between the creditor and the creditor agent, the creditor may be informed either through a negative CustomerPaymentStatusReport message, or through a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement') about the funds return and thus the debit on its account.

