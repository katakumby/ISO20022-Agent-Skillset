---
template: false
document_kind: "message-set-index"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
set_slug: "bank-to-customer-cash-management"
source_ids: ["src-000004", "src-000005", "src-000006", "src-000007", "src-000008", "src-000009", "src-000010"]
source_editions: ["2025-2026", "March 2026"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Bank-to-Customer Cash Management

This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.

## Supplied sources

| Source | Format | Publication label / evidence | Content identity / occurrences |
| --- | --- | --- | --- |
| [src-000004](../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx) | docx | March 2026 | 30d2ce6890b2a86b1eba40647d5f63cd4bd35a505aa062f359012a5ab523ec0a; 1 |
| [src-000005](../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf) | pdf | March 2026 | f6ea23ab7f761fc38ede7f596293d22a59e458aee42f2b0fbb9200ef1ef1ac9c; 1 |
| [src-000006](../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx) | xlsx | 2025-2026 | 1ca8a9cdb546449568f948d2115fd208c2b610e164daf96f9b905d2b8de9518b; 1 |
| [src-000007](../../../../../../raw-input/banktocustomer_cash_management/camt.052.001.14_0.xsd) | xsd | 2025-2026 | 8eedaf2f9f758d9f1323782fcfafbbeae4ec34a52acafd7925c5b86cd0a3a14b; 1 |
| [src-000008](../../../../../../raw-input/banktocustomer_cash_management/camt.053.001.14_0.xsd) | xsd | 2025-2026 | 4115741fcd10b4fc804349f960ac3f14bd88870ef7af51105488a319295cedf4; 1 |
| [src-000009](../../../../../../raw-input/banktocustomer_cash_management/camt.054.001.14_0.xsd) | xsd | 2025-2026 | 39b183f6689a869e9e002051c9180b2f298005502718278ec931c8a920af9a60; 1 |
| [src-000010](../../../../../../raw-input/banktocustomer_cash_management/camt.060.001.07.xsd) | xsd | 2025-2026 | 4af7f60be4175ae5fb333615a6029dcbc8400e3c5a70f9d418d82b8f2c510ade; 1 |

## Canonical message definitions

| Family | Exact definition | Membership evidence | Schema source |
| --- | --- | --- | --- |
| camt.052 | [camt.052.001.14](../../../messages/camt.052.001.14/index.md) | src-000005, src-000007 | src-000007 |
| camt.053 | [camt.053.001.14](../../../messages/camt.053.001.14/index.md) | src-000005, src-000008 | src-000008 |
| camt.054 | [camt.054.001.14](../../../messages/camt.054.001.14/index.md) | src-000005, src-000009 | src-000009 |
| camt.060 | [camt.060.001.07](../../../messages/camt.060.001.07/index.md) | src-000005, src-000010 | src-000010 |

## Focused evidence and context

| Reference | Kind | Review |
| --- | --- | --- |
| [src-000004](documents/src-000004/index.md) | documents | needs-review |
| [src-000005](documents/src-000005/index.md) | documents | needs-review |
| [src-000006](workbooks/src-000006/index.md) | workbooks | needs-review |
| [business-rules](business-rules.md) | curated context | see page |
| [participants-narrative](participants-narrative.md) | curated context | see page |
| [participants](participants.md) | curated context | see page |
| [source-consistency](source-consistency.md) | curated context | see page |
| [Flows](flows/index.md) | curated context | see page |

## Gaps

- All source tables and figures require recorded visual reconciliation before this set can be reviewed.

[Extraction coverage](coverage.md) · [Catalog](../../../../../../catalog/README.md)
