---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "CustomerDirectDebitInitiation and FIToFICustomerDirectDebit "]
content_origin: "source-transcription"
---

# CustomerDirectDebitInitiation and FIToFICustomerDirectDebit 

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path BusinessTransactions / CustomerDirectDebitInitiation and FIToFICustomerDirectDebit .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P198** CustomerDirectDebitInitiation and FIToFICustomerDirectDebit 

**P199** A Direct debit is a request for payment of an amount to be collected from a party bank account (the debtor) by an originator (the creditor). The amounts and dates of collections may vary.

**P200** Direct Debits result in cash transfers between debtors and creditors through infrastructures or correspondent banks. They may be exchanged as single instructions but are traditionally grouped following some common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode.

**P201** Direct Debits are processed in different ways from country to country, especially regarding the handling of the mandate (when it exists) given by the debtor to the creditor.

**P202** The CustomerDirectDebitInitiation message is sent by the initiating party (creditor) to the forwarding agent or creditor agent. It is used to request single or bulk collection(s) of cash from one or various debtor account(s) to a creditor.

**P203** The FIToFICustomerDirectDebit message is sent by a financial institution to another financial institution, directly or through a clearing system. It is used to clear Direct Debit instructions, initiated by non-financial institution customers.

**P204** Only the messages that are part of the scope of the direct debit are illustrated in the diagram.

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

**P206** To provide added value to its customer, a debtor agents may send the instruction (simplified version) to its customer, the debtor, for example, when pre-notifications are not used in a scheme.

**P207** The original mandate between the debtor and the creditor and the mandate management itself are identified as being out of scope and are therefore not included in the diagram. Some information on possible mandate management information flow is available below.

**P208** The mandate is the authorisation/expression of consent given by the debtor, allowing a specified creditor to originate direct debit instructions to debit a specified debtor account in accordance with the relevant direct debit Scheme Rules and, if applicable, the mandate details.

**P209** A valid/authorised mandate represents the debtor agreement to:

**P210** authorise the creditor to issue direct debit instruction(s) to the debtor account

**P211** instruct the debtor agent to act upon the creditor direct debit instruction

**P212** In some cases, the debtor agent is unaware of the mandate and simply acts upon the direct debit instruction.

**P213** A mandate can be an electronic mandate or a mandate in paper form. In case of a paper mandate the creditor dematerialises the mandate upon the mandate presentation in paper form. Dematerialised mandate data are referred to as the Mandate Related Information (MRI) only and are not to be considered as the mandate document. The original mandate remains subject for archiving and reference for any legal matter.

**P214** Prior to the sending of a direct debit instruction, the creditor may notify the debtor of the amount and date on which the direct debit instruction will be presented to the debtor agent for debit. This notification may be sent together with or separately from other commercial documents (for example, an invoice).

**P215** There are two types of pre-notifications:

**P216** Schedule of payments for a number of subsequent Direct Debits for an agreed period of time.

**P217** Individual advises of a direct debit subject for collection on a specified value date only. In case of recurrent

**P218** Direct Debit requires an update for each individual recurrent direct debit prior to its collection.

**P219** The debtor will reconcile the pre-notification with the signed/authorised mandate and where relevant other records (such as account payable items, contract details or subscription agreement). The debtor ensures the account is covered with subject amount.

**P220** The creditor sends the CustomerDirectDebitInitiation message to its agent (the creditor agent), together with the Mandate Related Information when requested by the scheme.

**P221** The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when requested by the scheme.

**P222** The clearing and settlement agent sends the FIToFICustomerDirectDebit message, together with the Mandate Related Information (MRI), when requested by the scheme, to the debtor agent.

**P223** Out of scope 

**P224** Optionally, the debtor agent could forward the direct debit instruction (simplified version) to the debtor (for example, if pre-notifications are not used in a scheme).

**P225** If the clearing and settlement agent are two parties the clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the Settlement Agent.

**P226** The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

**P227** The clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the settlement agent.

**P228** The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

**P229** The settlement is executed by the settlement agent, in accordance with the settlement cycle, based on the settlement report provided by the clearing agent. The settlement agent performs the transfer of funds from the debtor agent to the creditor agent.

**P230** Reporting (BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement')) to the debtors and creditors is out of scope. Timing may vary depending on market practices and value added services provided by some agents, that is, before or after settlement.

