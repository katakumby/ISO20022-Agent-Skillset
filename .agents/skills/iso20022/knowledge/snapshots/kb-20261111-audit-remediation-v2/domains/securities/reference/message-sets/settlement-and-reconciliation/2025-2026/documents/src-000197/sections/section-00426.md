---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.16 OtherBusinessParties <OthrBizPties>", "19.4.17.1 CertificationIdentification <CertfctnId>"]
file_pages: [652]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.17.1 CertificationIdentification <CertfctnId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 652 to 652.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 652

```text
AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls> contains the following
RegistrationParameters6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CertificationIdentification <CertfctnId> [0..1] Text 652
   CertificationDateTime <CertfctnDtTm> [0..1] ± 652
   RegistrarAccount <RegarAcct> [0..1] Text 652
   CertificateNumber <CertNb> [0..*] ± C27 652
19.4.17.1  CertificationIdentification <CertfctnId>
Presence: [0..1]
Definition: Identification assigned to a deposit.
Datatype: "Max35Text" on page 2192
19.4.17.2  CertificationDateTime <CertfctnDtTm>
Presence: [0..1]
Definition: Date/time at which the certificates in the deposit were validated by the agent.
CertificationDateTime <CertfctnDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
19.4.17.3  RegistrarAccount <RegarAcct>
Presence: [0..1]
Definition: Account at the registrar where financial instruments are registered.
Datatype: "Max35Text" on page 2192
19.4.17.4  CertificateNumber <CertNb>
Presence: [0..*]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Impacted by: C27 "ISO8532AndIssuerSchemeNameRule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 652 March 2026
```

