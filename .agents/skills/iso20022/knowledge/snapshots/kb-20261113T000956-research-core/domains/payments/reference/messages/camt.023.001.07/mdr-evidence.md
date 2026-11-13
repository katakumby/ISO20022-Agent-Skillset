---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.023.001.07"
message_family: "camt.023"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "21 camt.023.001.07 BackupPaymentV07", "file_pages": [577, 590]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.023.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 21 camt.023.001.07 BackupPaymentV07

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp577–590; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 21 camt.023.001.07 BackupPaymentV07, Functionality, file p577.**

Scope
The BackupPayment message is sent by a member to the transaction administrator.
It is used to request a liquidity transfer from the member to another participant in the system when the
user is in recovery mode.
Usage
Under very specific circumstances, the transaction administrator can accept direct input of transactions
as part of its cash management functionalities. This possibility is available only when a declared
incident has been reported to the transaction administrator This could be the case, for example, when
the internal systems of the member are having problems sending out payments or when the continuity
of the whole system is put at risk.
The purpose of the BackupPayment message is to prevent the consequences of a specific failure
affecting not only the member experiencing problems but also its counterparties. Members can
therefore input transactions directly in order to ensure the stability of the system and smooth
exchanges.
At any time during the operating hours of the system, and under the agreed circumstances, the member
can request a backup payment to be effected.
The member can request the transfer by identifying the following elements:
- party (account owner) that will receive the funds
- the financial institution that will receive the funds on behalf of the account owner
Based on the criteria received within the BackupPayment message, the transaction administrator will
execute or reject the requested funds transfer.
The transaction administrator may send a Receipt message as a reply to the BackupPayment request.
To verify the outcome of the request, the member may submit a GetTransaction or GetAccount
message with the appropriate search criteria.
Outline
The BackupPaymentV07 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. OriginalMessageIdentification
Identifies the original message identification.
This was formerly the PaymentInstructionReference.
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 577 February 2025

**src-000015, 21 camt.023.001.07 BackupPaymentV07, Functionality, file p578.**

C. InstructionInformation
Provides details on the execution and type of payment contained in the instruction.
D. TransferredAmount
Quantity of cash that the transaction administrator transfers from one account to another.
E. Creditor
Party that receives an amount of money from the debtor.
F. CreditorAgent
Financial institution that receives the payment transaction on behalf of an account owner, or other
nominated party, and credits the account.
G. DebtorAgent
Financial institution that receives the payment transaction from the account owner, or other
authorised party, and processes the instruction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 578 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [21 camt.023.001.07 BackupPaymentV07](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00423.md) | 577–578 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00424.md) | 579–579 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00425.md) | 580–580 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.3 InstructionInformation &lt;InstrInf&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00426.md) | 581–582 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.3 InstructionInformation &lt;InstrInf&gt; / 21.4.3.2 PaymentType &lt;PmtTp&gt; / 21.4.3.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00427.md) | 583–583 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.5 Creditor &lt;Cdtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00428.md) | 584–584 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.5 Creditor &lt;Cdtr&gt; / 21.4.5.2 MemberIdentification &lt;MmbId&gt; / 21.4.5.2.2 ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00429.md) | 585–585 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.6 CreditorAgent &lt;CdtrAgt&gt; / 21.4.6.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00430.md) | 586–586 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.6 CreditorAgent &lt;CdtrAgt&gt; / 21.4.6.2 MemberIdentification &lt;MmbId&gt; / 21.4.6.2.2 ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00431.md) | 587–587 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.7 DebtorAgent &lt;DbtrAgt&gt; / 21.4.7.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00432.md) | 588–588 |
| [21 camt.023.001.07 BackupPaymentV07 / 21.4 Message Building Blocks / 21.4.7 DebtorAgent &lt;DbtrAgt&gt; / 21.4.7.2 MemberIdentification &lt;MmbId&gt; / 21.4.7.2.2 ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00433.md) | 589–590 |

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

- [Backup Payment Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p181-backup-payment-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
