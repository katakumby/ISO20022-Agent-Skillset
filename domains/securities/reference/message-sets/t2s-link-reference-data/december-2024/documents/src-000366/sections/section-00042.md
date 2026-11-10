---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["6 reda.050.001.01 AccountLinkMaintenanceRequestV01", "6.4 Message Building Blocks", "6.4.2 AccountLinkIdentification <AcctLkId>", "6.4.2.1 SecuritiesAccount <SctiesAcct>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 6.4.2.1 SecuritiesAccount <SctiesAcct>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
6.4.2.1  SecuritiesAccount <SctiesAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SecuritiesAccount <SctiesAcct> contains the following elements (see "SecuritiesAccount19" on
page 59 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 59
   Type <Tp> [0..1] ± 59
   Name <Nm> [0..1] Text 59
6.4.2.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 65 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   Type <Tp> [0..1] ± 65
   Name <Nm> [0..1] Text 65
6.4.2.3  CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
CashAccount <CshAcct> contains the following elements (see "CashAccount38" on page 55 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 55
   Type <Tp> [0..1] ± 55
   Currency <Ccy> [0..1] CodeSet C1 55
   Name <Nm> [0..1] Text 56
   Proxy <Prxy> [0..1] ± 56
6.4.2.4  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the securities account is linked to the cash account.
Approved by the Securities SEG on 21 November 2024. reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 44 December 2024
```

