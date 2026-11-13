---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope"]
content_origin: "source-transcription"
---

# Scope

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path Scope and Functionality / Scope.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P68** Scope

**P69** In recent years, the need for financial institutions to manage payment transactions intra-day in real-time across currencies has become a reality. Financial institutions face growing volumes in domestic and cross-border real-time payment settlement systems. They must have the means to adequately address the following areas of concern: the increased regulatory pressure on managing settlement risk, monitoring the centralisation of liquidity management and treasury functions and the integration of securities settlement systems with payment settlement systems.

**P70** Clients that are not financial institutions, in turn, will be expressing similar needs, and expect their service providers to offer such capabilities. These needs translate into a requirement to have the ability to obtain near real-time information on account balances and transactions held with account servicing institutions, whether they are individual financial institutions or clearing and settlement systems. It may also require more advanced services, such as the ability to cancel, suspend or modify, in near real-time, payment transactions with service providers and settlement systems, in order to better manage risk and liquidity.

**P71** In addition to the implementation of payment-processing applications that are capable of operating in a real-time environment, and account owners implementing risk and liquidity management applications capable of using the information provided, solutions will be required to transport and deliver the information.

**P72** The solutions available to the banking industry to address these needs, are currently proving unsatisfactory, either due to a lack of standardisation in the case of proprietary solutions, or due to the lack of suitable standards and real-time capabilities in the case of industry solutions, such as SWIFT's FIN messaging.

**P73** Driven by the aforementioned business rationale, SWIFT has developed the Cash Management set of messages. This Message Definition Report describes a standardised message set, covering the cash management business area, cash reporting transaction management and the exchange of information on the cash side of financial transactions.

**P74** The scope of the Cash Management messages set is very varied. It ranges from information on transactions and balances to actions to manage flow of transactions submitted by the member to the transaction administrator, but also from information on the system status and features to actions to manage the liquidity and reservation limits.

**P75** These messages may be exchanged at pre-agreed times, upon request of the account owner or at the initiative of the account servicing institution, that is either triggered by a request from the account owner ('pull' mechanism), or initiated by the account servicing institution ('push' mechanism).

**P76** All the messages in the Cash Management set have a common purpose: to cater for the exchange of information between an account owner and its account servicing institution.

**P77** It is important to realise that the term 'account owner' can refer either to a financial institution, or to a corporate customer or to a private individual, and that the term 'account servicing institutioni is referring to either a financial institution or to a clearing system operator.

**P78** Taking this into account, it seems logical to infer that a '(direct) member' can be simply an account owner that is entitled to input transactions on its own behalf and/or on behalf of its customers, and that a 'transaction administrator' is the account servicing institution.Groups of MessageDefinitions and Functionality

