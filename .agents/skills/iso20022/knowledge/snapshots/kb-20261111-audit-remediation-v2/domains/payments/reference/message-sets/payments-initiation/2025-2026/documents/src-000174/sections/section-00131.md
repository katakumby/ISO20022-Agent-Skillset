---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.7 SettlementInformation <SttlmInf>", "3.4.3.7.12.7.8 ThirdReimbursementAgent <ThrdRmbrsmntAgt>"]
file_pages: [198]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.7.8 ThirdReimbursementAgent <ThrdRmbrsmntAgt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 198 to 198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 198

```text
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
3.4.3.7.12.7.8  ThirdReimbursementAgent <ThrdRmbrsmntAgt>
Presence: [0..1]
Definition: Agent at which the instructed agent will be reimbursed.
Usage: If ThirdReimbursementAgent contains a branch of the InstructedAgent, then the party in
InstructedAgent will claim reimbursement from that branch/will be paid by that branch.
ThirdReimbursementAgent <ThrdRmbrsmntAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 539 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  540
     BICFI <BICFI> [0..1] IdentifierSet C4 540
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 541
     LEI <LEI> [0..1] IdentifierSet 541
     Name <Nm> [0..1] Text 541
     PostalAddress <PstlAdr> [0..1] ± 541
     Other <Othr> [0..1] ± 542
   BranchIdentification <BrnchId> [0..1]  543
     Identification <Id> [0..1] Text 543
     LEI <LEI> [0..1] IdentifierSet 543
     Name <Nm> [0..1] Text 543
     PostalAddress <PstlAdr> [0..1] ± 543
3.4.3.7.12.7.9  ThirdReimbursementAgentAccount <ThrdRmbrsmntAgtAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the third reimbursement agent account at its
servicing agent in the payment chain.
Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 198 March 2026
```

