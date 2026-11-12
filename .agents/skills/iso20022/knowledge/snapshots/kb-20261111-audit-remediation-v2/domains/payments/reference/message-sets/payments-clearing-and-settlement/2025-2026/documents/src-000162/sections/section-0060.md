---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Direct Debit", "FIToFICustomerDirectDebit"]
content_origin: "source-transcription"
---

# FIToFICustomerDirectDebit

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path BusinessTransactions / Direct Debit / FIToFICustomerDirectDebit.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P468** FIToFICustomerDirectDebit

**P469** A direct debit is a request for payment of an amount to be collected from a party bank account (the debtor account) by an originator (the creditor). The amounts and dates of collections may vary.

**P470** Direct debits result in cash transfers between debtor and creditor through infrastructures or correspondent banks. They may be exchanged as single instructions but are traditionally grouped following some common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode.

**P471** Direct debits are processed in different ways from country to country, especially regarding the handling of the mandate (when it exists) given by the debtor to the creditor.

**P472** The CustomerDirectDebitInitiation message is sent by the Initiating party (creditor) to the forwarding agent or creditor agent. It is used to request single or bulk collection(s) of cash from one or various debtor account(s) to a creditor. The CustomerDirectDebitInitiation is only shown in the diagram for information purpose. The focus of this document is on the interbank processing of the FIToFICustomerDirectDebit message.

**P473** The FIToFICustomerDirectDebit message is sent by a financial institution to another financial institution, directly or through a Clearing System. It is used to clear direct debit instructions, initiated by non-financial institution customers.

[fig-0037 - original figure evidence](../diagrams/fig-0037.md)

**P475** As added value to customers, some debtor agents send the instructions (simplified version) to their customers, the debtors, for example, if pre-notifications are not used in a scheme

**P476** The original mandate between the debtor and the creditor and the mandate management itself are identified as being out of scope and are therefore not included in the diagram. Some information on possible mandate management information flow is available below.

**P477** The mandate is the authorisation/expression of consent given by the debtor, allowing a specified creditor to originate direct debit instructions to debit a specified debtor account in accordance with the relevant Direct Debit Scheme Rules and, if applicable, the mandate details.

**P478** A valid/authorised mandate represents the debtor agreement:

**P479** to authorise the creditor to issue direct debit instruction(s) to the debtor account, and;

**P480** to instruct the debtor agent to act upon the creditor direct debit instruction.

**P481** In some cases, the debtor agent is unaware of the Mandate and simply acts upon the direct debit instruction. A mandate can be an electronic mandate or a mandate in paper form. In case of a paper mandate the creditor dematerialises the mandate upon the mandate presentation in paper form. Dematerialised mandate data are referred to as the Mandate Related Information (MRI) only and are not to be considered as the mandate document. The original mandate remains subject for archiving and reference for any legal matter.

**P482** Prior to the sending of a direct debit instruction, the creditor may notify the debtor of the amount and date on which the direct debit instruction will be presented to the debtor agent for debit. This notification may be sent together with or separately from other commercial documents (for example, an invoice).

**P483** There are two types of pre-notifications:

**P484** Schedule of payments for a number of subsequent direct debits for an agreed period of time.

**P485** Individual advises of a direct debit subject for collection on a specified value date only. In the case of a recurrent direct debit. This requires an update for each individual recurrent direct debit prior to its collection.

**P486** The debtor will reconcile the pre-notification with the signed/authorised mandate and where relevant other records (such as account payable items, contract details or subscription agreement). The debtor ensures the account is covered with subject amount.

**P487** The creditor sends the CustomerDirectDebitInitiation message to its agent (the creditor agent), together with the Mandate Related Information when requested by the scheme.

**P488** The creditor agent sends an FIToFICustomerDirectDebit message to the Clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when requested by the scheme.

**P489** The clearing and settlement agent send the FIToFICustomerDirectDebit message, together with the Mandate Related Information (MRI), when requested by the scheme, to the debtor agent.

**P490** The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

**P491** The settlement is executed by the settlement agent, in accordance with the settlement cycle, based on the settlement report provided by the clearing agent. The settlement agent performs the transfer of funds from the debtor agent to the creditor agent.

**P492** Out of scope

**P493** The debtor agent could optionally forward the direct debit instruction (simplified version) to the debtor (for example, in case pre-notifications are not used in a Scheme).

**P494** If clearing and settlement is carried out by two parties, the clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the settlement agent.

**P495** Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages) to the debtors and creditors. Timing may vary depending on market practices and value added services provided by some agents that are before or after settlement.

