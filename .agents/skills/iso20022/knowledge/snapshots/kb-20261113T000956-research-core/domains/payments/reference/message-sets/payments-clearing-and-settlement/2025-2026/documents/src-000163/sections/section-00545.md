---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.14 MandateRelatedInformation <MndtRltdInf>"]
file_pages: [749]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.14 MandateRelatedInformation <MndtRltdInf>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 749 to 749.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 749

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification3" on page 1184 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1185
   Issuer <Issr> [0..1] Text 1185
6.4.2.14  MandateRelatedInformation <MndtRltdInf>
Presence: [0..1]
Definition: Provides further details of the mandate signed between the creditor and the debtor.
MandateRelatedInformation <MndtRltdInf> contains the following elements (see
"CreditTransferMandateData1" on page 1169 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 1169
   Type <Tp> [0..1] ± 1169
   DateOfSignature <DtOfSgntr> [0..1] Date 1170
   DateOfVerification <DtOfVrfctn> [0..1] DateTime 1170
   ElectronicSignature <ElctrncSgntr> [0..1] Binary 1170
   FirstPaymentDate <FrstPmtDt> [0..1] Date 1170
   FinalPaymentDate <FnlPmtDt> [0..1] Date 1170
   Frequency <Frqcy> [0..1] ± 1171
   Reason <Rsn> [0..1]  1171
{Or     Code <Cd> [1..1] CodeSet 1171
Or}     Proprietary <Prtry> [1..1] Text 1171
6.4.2.15  PaymentSignature <PmtSgntr>
Presence: [0..1]
Definition: Cryptographic key identifying terms agreed by agents within the payment chain pre-
settlement. This key can also be used post-settlement to confirm the payment has been credited as
intended.
PaymentSignature <PmtSgntr> contains one of the following CryptographicKey1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ILPV4 <ILPV4> [1..1] Text 750
Or}   Signature <Sgntr> [1..1] Text 750
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
749 March 2026
```

