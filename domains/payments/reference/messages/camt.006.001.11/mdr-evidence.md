---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.006.001.11"
message_family: "camt.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.006.001.11"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "5 camt.006.001.11 ReturnTransactionV11", "file_pages": [206, 325]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.006.001.11 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 5 camt.006.001.11 ReturnTransactionV11

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp206–325; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 5 camt.006.001.11 ReturnTransactionV11, Functionality, file p206.**

Scope
The ReturnTransaction message is sent by the transaction administrator to a member of the system.
It is used to provide information on transactions and booked entries held at the transaction
administrator.
The Return Transaction message can be sent as a response to a related GetTransaction message (pull
mode) or initiated by the transaction administrator (push mode). The push of information can take place
either at prearranged times or as a warning or alarm when a problem has occurred.
Usage
Following normal business flows, transactions registered by the transaction administrator may be
queued for later settlement (because of insufficient funds available, because of risk or liquidity limits,
etc.). A transaction may have a series of statuses. These can be transient (such as pending or related
types) and final (such as rejected or settled).
Members of a system need to receive information about the payments queue(s) and must have the
ability to take action (that is, cancel or modify the transaction(s) to be settled). Note, however, that
actions by a member will always concern transactions in a transient status.
At any time during operating hours of the system, the member can query the transaction administrator
to get information about transactions, whatever their status.
These requests will concern either all transactions, all transactions within a particular status or a
specific transaction.
The member can request information about transactions through a series of criteria, corresponding to
the known information stored within the transaction administrator. Based on the criteria received within
the request, the transaction administrator will select items that match the request and report them to the
requester.
The transaction administrator may also send a ReturnTransaction message with pre-defined
information at times previously agreed with the member or to warn the member about a particular
problem that may have arisen and which needs attention.
The message from the transaction administrator can contain information based on the following
elements:
- provenance or destination of the payment (payment to/payment from)
- transaction reference
- transfer value date
- payment instruction reference
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 206 February 2025

**src-000015, 5 camt.006.001.11 ReturnTransactionV11, Functionality, file p207.**

- payment instruction status, as registered at the transaction administrator
- instructed amount and/or currency
- interbank settlement amount and/or currency
- credit/debit indicator of the payment instruction/transaction
- message used for the payment instruction
- priority of the payment transaction
- period in which the payment instruction should be processed (processing validity time)
- instructions given, related to the processing of the transaction
- type of payment instructed
- account identification (entries booked to a specific account)
- entry amount and/or currency
- entry debit/credit indicator (if absent, all entries should be reported)
- status of the entry (pending, booked.)
- entry date and time
- currency of the account
- type of the account
- entry reference
- entry date
- transfer reason
- details related to the status of the payment instruction
An element that is particular to the Get/Return Transaction pair is the Statement Report. When a
GetTransaction message is sent requesting a statement report, the related ReturnTransaction message
will provide a pre-defined set of return criteria per transaction. The information returned contains the
following details for each transaction:
- value date
- entry date
- debit/credit code
- entry amount
- method of payment (payment instrument or message type)
- entry reference
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 207 February 2025

**src-000015, 5 camt.006.001.11 ReturnTransactionV11, Functionality, file p208.**

- transaction reference
- supplementary details
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The ReturnTransactionV11 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on transactions.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 208 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 camt.006.001.11 ReturnTransactionV11](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00133.md) | 206–208 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00134.md) | 209–214 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00135.md) | 215–216 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00136.md) | 217–223 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00137.md) | 224–230 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00138.md) | 231–232 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.1 PaymentFrom &lt;PmtFr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00139.md) | 233–233 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.1 PaymentFrom &lt;PmtFr&gt; / 5.4.2.1.1.1.3 Country &lt;Ctry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00140.md) | 234–234 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.2 PaymentTo &lt;PmtTo&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00141.md) | 235–235 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.2 PaymentTo &lt;PmtTo&gt; / 5.4.2.1.1.2.3 Country &lt;Ctry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00142.md) | 236–236 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00143.md) | 237–237 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt; / 5.4.2.1.1.3.1 Code &lt;Cd&gt; / 5.4.2.1.1.3.1.1 Pending &lt;Pdg&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00144.md) | 238–238 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt; / 5.4.2.1.1.3.1 Code &lt;Cd&gt; / 5.4.2.1.1.3.1.2 Final &lt;Fnl&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00145.md) | 239–239 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt; / 5.4.2.1.1.3.3 Reason &lt;Rsn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00146.md) | 240–241 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt; / 5.4.2.1.1.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.1.3.3.2 Cancelled &lt;Canc&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00147.md) | 242–244 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt; / 5.4.2.1.1.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.1.3.3.5 PendingSettlement &lt;PdgSttlm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00148.md) | 245–246 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt; / 5.4.2.1.1.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.1.3.3.6 ProprietaryRejection &lt;PrtryRjctn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00149.md) | 247–247 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.3 CommonStatus &lt;CmonSts&gt; / 5.4.2.1.1.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.1.3.3.7 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00150.md) | 248–248 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.1 PaymentCommonInformation &lt;PmtCmonInf&gt; / 5.4.2.1.1.7 PaymentMethod &lt;PmtMtd&gt; / 5.4.2.1.1.7.1 FINMessageType &lt;FINMT&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00151.md) | 249–249 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.2 TransactionsSummary &lt;TxsSummry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00152.md) | 250–250 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.2 TransactionsSummary &lt;TxsSummry&gt; / 5.4.2.1.2.3 TotalNetEntryAmount &lt;TtlNetNtryAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00153.md) | 251–255 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00154.md) | 256–256 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00155.md) | 257–257 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.2 UETR &lt;UETR&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00156.md) | 258–258 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 5.4.2.1.3.1.4.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00157.md) | 259–259 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 5.4.2.1.3.1.4.3 InterbankSettlementAmount &lt;IntrBkSttlmAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00158.md) | 260–260 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 5.4.2.1.3.1.4.6 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00159.md) | 261–261 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 5.4.2.1.3.1.4.7 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00160.md) | 262–262 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 5.4.2.1.3.1.4.8 EntryType &lt;NtryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00161.md) | 263–263 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.5 ShortBusinessIdentification &lt;ShrtBizId&gt; / 5.4.2.1.3.1.5.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00162.md) | 264–264 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.1 PaymentIdentification &lt;PmtId&gt; / 5.4.2.1.3.1.6 ProprietaryIdentification &lt;PrtryId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00163.md) | 265–268 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00164.md) | 269–272 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.1 PaymentTo &lt;PmtTo&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00165.md) | 273–273 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.1 PaymentTo &lt;PmtTo&gt; / 5.4.2.1.3.2.1.1.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00166.md) | 274–274 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.1 PaymentTo &lt;PmtTo&gt; / 5.4.2.1.3.2.1.1.4 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00167.md) | 275–275 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.2 PaymentFrom &lt;PmtFr&gt; / 5.4.2.1.3.2.1.2.3 Country &lt;Ctry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00168.md) | 276–276 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.3 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00169.md) | 277–279 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00170.md) | 280–280 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.3 Status &lt;Sts&gt; / 5.4.2.1.3.2.1.4.3.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00171.md) | 281–282 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.3 Status &lt;Sts&gt; / 5.4.2.1.3.2.1.4.3.1 Code &lt;Cd&gt; / 5.4.2.1.3.2.1.4.3.1.2 Final &lt;Fnl&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00172.md) | 283–283 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.3 Status &lt;Sts&gt; / 5.4.2.1.3.2.1.4.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.3.2.1.4.3.3.1 Unmatched &lt;Umtchd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00173.md) | 284–285 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.3 Status &lt;Sts&gt; / 5.4.2.1.3.2.1.4.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.3.2.1.4.3.3.2 Cancelled &lt;Canc&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00174.md) | 286–288 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.3 Status &lt;Sts&gt; / 5.4.2.1.3.2.1.4.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.3.2.1.4.3.3.5 PendingSettlement &lt;PdgSttlm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00175.md) | 289–290 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.3 Status &lt;Sts&gt; / 5.4.2.1.3.2.1.4.3.3 Reason &lt;Rsn&gt; / 5.4.2.1.3.2.1.4.3.3.6 ProprietaryRejection &lt;PrtryRjctn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00176.md) | 291–291 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.4 InstructedAmount &lt;InstdAmt&gt; / 5.4.2.1.3.2.1.4.4.1 AmountWithCurrency &lt;AmtWthCcy&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00177.md) | 292–292 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.7 PaymentMethod &lt;PmtMtd&gt; / 5.4.2.1.3.2.1.4.7.1 FINMessageType &lt;FINMT&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00178.md) | 293–293 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.8 Priority &lt;Prty&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00179.md) | 294–294 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.9 ProcessingValidityTime &lt;PrcgVldtyTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00180.md) | 295–295 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.11 Type &lt;Tp&gt; / 5.4.2.1.3.2.1.4.11.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00181.md) | 296–296 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.11 Type &lt;Tp&gt; / 5.4.2.1.3.2.1.4.11.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00182.md) | 297–297 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.12 GeneratedOrder &lt;GnrtdOrdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00183.md) | 298–298 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.1 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00184.md) | 299–299 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.2 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00185.md) | 300–300 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.3 UltimateDebtor &lt;UltmtDbtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00186.md) | 301–301 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.3 UltimateDebtor &lt;UltmtDbtr&gt; / 5.4.2.1.3.2.1.4.16.3.2 Agent &lt;Agt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00187.md) | 302–302 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.4 Debtor &lt;Dbtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00188.md) | 303–303 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.4 Debtor &lt;Dbtr&gt; / 5.4.2.1.3.2.1.4.16.4.2 Agent &lt;Agt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00189.md) | 304–304 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.5 DebtorAgent &lt;DbtrAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00190.md) | 305–305 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.6 InstructingReimbursementAgent &lt;InstgRmbrsmntAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00191.md) | 306–306 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.7 InstructedReimbursementAgent &lt;InstdRmbrsmntAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00192.md) | 307–307 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.9 IntermediaryAgent2 &lt;IntrmyAgt2&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00193.md) | 308–308 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.10 IntermediaryAgent3 &lt;IntrmyAgt3&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00194.md) | 309–309 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.11 CreditorAgent &lt;CdtrAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00195.md) | 310–310 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.12 Creditor &lt;Cdtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00196.md) | 311–311 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.12 Creditor &lt;Cdtr&gt; / 5.4.2.1.3.2.1.4.16.12.2 Agent &lt;Agt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00197.md) | 312–312 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.13 UltimateCreditor &lt;UltmtCdtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00198.md) | 313–313 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.4 Payment &lt;Pmt&gt; / 5.4.2.1.3.2.1.4.16 Parties &lt;Pties&gt; / 5.4.2.1.3.2.1.4.16.13 UltimateCreditor &lt;UltmtCdtr&gt; / 5.4.2.1.3.2.1.4.16.13.2 Agent &lt;Agt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00199.md) | 314–314 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00200.md) | 315–315 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt; / 5.4.2.1.3.2.1.5.1 Account &lt;Acct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00201.md) | 316–316 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt; / 5.4.2.1.3.2.1.5.1 Account &lt;Acct&gt; / 5.4.2.1.3.2.1.5.1.1 Identification &lt;Id&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00202.md) | 317–317 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt; / 5.4.2.1.3.2.1.5.1 Account &lt;Acct&gt; / 5.4.2.1.3.2.1.5.1.4 Name &lt;Nm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00203.md) | 318–318 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt; / 5.4.2.1.3.2.1.5.1 Account &lt;Acct&gt; / 5.4.2.1.3.2.1.5.1.7 Servicer &lt;Svcr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00204.md) | 319–319 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt; / 5.4.2.1.3.2.1.5.2 Entry &lt;Ntry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00205.md) | 320–320 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt; / 5.4.2.1.3.2.1.5.2 Entry &lt;Ntry&gt; / 5.4.2.1.3.2.1.5.2.2 Date &lt;Dt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00206.md) | 321–321 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.5 AccountEntry &lt;AcctNtry&gt; / 5.4.2.1.3.2.1.5.2 Entry &lt;Ntry&gt; / 5.4.2.1.3.2.1.5.2.4 Identification &lt;Id&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00207.md) | 322–322 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.1 Transaction &lt;Tx&gt; / 5.4.2.1.3.2.1.6 SecuritiesTransactionReferences &lt;SctiesTxRefs&gt; / 5.4.2.1.3.2.1.6.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00208.md) | 323–323 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.1 BusinessReport &lt;BizRpt&gt; / 5.4.2.1.3 TransactionReport &lt;TxRpt&gt; / 5.4.2.1.3.2 TransactionOrError &lt;TxOrErr&gt; / 5.4.2.1.3.2.2 BusinessError &lt;BizErr&gt; / 5.4.2.1.3.2.2.1 Error &lt;Err&gt; / 5.4.2.1.3.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00209.md) | 324–324 |
| [5 camt.006.001.11 ReturnTransactionV11 / 5.4 Message Building Blocks / 5.4.2 ReportOrError &lt;RptOrErr&gt; / 5.4.2.2 OperationalError &lt;OprlErr&gt; / 5.4.2.2.1 Error &lt;Err&gt; / 5.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00210.md) | 325–325 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [ACH](../../../../../shared/reference/participants/participant-src-000014-ach.md) | participant | src-000014 |
| [Automated Clearing House (ACH)](../../../../../shared/reference/participants/participant-src-000014-automated-clearing-house-ach.md) | participant | src-000014 |
| [Cash Provider](../../../../../shared/reference/participants/participant-src-000014-cash-provider.md) | participant | src-000014 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000014-central-securities-depositories-csd.md) | participant | src-000014 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000014-corporate.md) | participant | src-000014 |
| [CSD](../../../../../shared/reference/participants/participant-src-000014-csd.md) | participant | src-000014 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000014-market-infrastructure.md) | participant | src-000014 |
| [Real Time Gross Settlement System (RTGS)](../../../../../shared/reference/participants/participant-src-000014-real-time-gross-settlement-system-rtgs.md) | participant | src-000014 |
| [RTGS](../../../../../shared/reference/participants/participant-src-000014-rtgs.md) | participant | src-000014 |
| [Settlement Agent](../../../../../shared/reference/participants/participant-src-000014-settlement-agent.md) | participant | src-000014 |
| [System Member](../../../../../shared/reference/participants/participant-src-000014-system-member.md) | participant | src-000014 |
| [System / Transaction Administrator](../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | participant | src-000014 |
| [Transaction Administrator/System](../../../../../shared/reference/participants/participant-src-000014-transaction-administrator-system.md) | participant | src-000014 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- CASH-FLOWS -->
## Operational Cash Management flows

- [Get/Return Transaction](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p186-get-return-transaction.md)
- [Get/Return Transaction Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p190-get-return-transaction-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
