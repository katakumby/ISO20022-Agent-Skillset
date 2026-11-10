---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.17 OtherBusinessParties <OthrBizPties>", "17.4.18.1 CertificationIdentification <CertfctnId>"]
file_pages: [554, 555]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.18.1 CertificationIdentification <CertfctnId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 554 to 555.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 554

```text
17.4.18.1  CertificationIdentification <CertfctnId>
Presence: [0..1]
Definition: Identification assigned to a deposit.
Datatype: "Max35Text" on page 2192
17.4.18.2  CertificationDateTime <CertfctnDtTm>
Presence: [0..1]
Definition: Date/time at which the certificates in the deposit were validated by the agent.
CertificationDateTime <CertfctnDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
17.4.18.3  RegistrarAccount <RegarAcct>
Presence: [0..1]
Definition: Account at the registrar where financial instruments are registered.
Datatype: "Max35Text" on page 2192
17.4.18.4  CertificateNumber <CertNb>
Presence: [0..*]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Impacted by: C36 "ISO8532AndIssuerSchemeNameRule"
CertificateNumber <CertNb> contains the following elements (see "SecuritiesCertificate4" on
page 1630 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Text 1631
   Issuer <Issr> [0..1] Text 1631
   SchemeName <SchmeNm> [0..1] Text 1631
Constraints
• ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
17.4.19 SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 554 March 2026
```

## File page 555

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C74 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 555 March 2026
```

