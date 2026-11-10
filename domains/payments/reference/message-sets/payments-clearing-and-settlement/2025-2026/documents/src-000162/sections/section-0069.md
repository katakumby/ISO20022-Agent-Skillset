---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FIToFIPaymentReversal with Direct Debit "]
content_origin: "source-transcription"
---

# FIToFIPaymentReversal with Direct Debit 

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Direct Debit / FIToFIPaymentReversal with Direct Debit .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P556** FIToFIPaymentReversal with Direct Debit 

**P557** The creditor can initiate a CustomerPaymentReversal message, after settlement, when a paid direct debit should not have been processed.

**P558** The creditor agent will, in turn, initiate an FIToFIPaymentReversal for the next agent in the payment chain. Consequently, the debtor will be credited.

**P559** The creditor agent may be the originator of a payment reversal - it will in this case initiate a FIToFIPaymentReversal message.

**P560** The creditor sends (for example) a CustomerDirectDebitInitiation message to its agent (the creditor agent). (Only potential messages, part of the direct debit scope are illustrated in the sequence diagram). 

[fig-0042 - original figure evidence](../diagrams/fig-0042.md)

**P562** The creditor agent can confirm the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

**P563** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

**P564** The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P565** The clearing and settlement agent sends an FIToFICustomerDirectDebit message, together with potentially the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

**P566** The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. The creditor realises this was a duplicated CustomerDirectDebitInitiation instruction. It now wants to send a CustomerPaymentReversal message. It identifies the original CustomerDirectDebitInitiation message (or a file of direct debit instructions) and generates an offsetting transaction in favour of the debtor, under the quotation of the reversal reasons. The creditor agent may confirm the receipt of the CustomerPaymentReversal message by sending a positive CustomerPaymentStatusReport message to the creditor.

**P567** An FIToFIPaymentReversal message is submitted by the creditor agent to the clearing and settlement agent for settlement, under quotation of the original direct debit reference and the reason for the reversal for example, in case of duplicated direct debit instruction.

**P568** The clearing agent confirms the processability of the reversal by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

**P569** The clearing and settlement agent forwards the FIToFIPaymentReversal message to the debtor agent immediately for information purposes only.

**P570** If clearing and settlement is carried out by two parties, the clearing agent prepares the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). That process includes the calculation of the settlement positions.

**P571** The information provided to the settlement agent is the net position to be debited, the party to be debited, the net position to the credited, the party to be credited and the value date (Out of Scope).

**P572** The settlement agent performs the transfer of funds from the credit party to the debit party (in accordance with the agreed and published settlement cycle) (out of scope).

**P573** A positive FIToFIPaymentStatusReport message can optionally be initiated by the debtor agent and sent to the clearing and settlement agent to confirm the processability of the reversal message.

**P574** It may exceptionally occur that a PaymentReturn message and an FIToFIPaymentReversal message would cross each other, but this could only be avoided through value-added monitoring services that could be offered by the scheme manager and/or might provoke exceptions/investigation handling.

