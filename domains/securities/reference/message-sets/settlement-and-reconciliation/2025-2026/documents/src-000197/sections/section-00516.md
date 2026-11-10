---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10"]
file_pages: [783, 784]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 783 to 784.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 783

```text
24 sese.030.001.10
SecuritiesSettlementConditionsModificationR
equestV10
24.1 MessageDefinition Functionality
Scope
An account owner sends a SecuritiesSettlementConditionsModificationRequest to an account servicer
to request the modification of a processing indicator or another non-matching information.
The account owner/servicer relationship may be:
- a central securities depository participant which has an account with a central securities depository.
It could also be, if agreed in a service level agreement:
- a global custodian which has an account with its local agent (sub-custodian), or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
In markets where this applies (for example, securities market infrastructures with no pre-settlement
matching process), it is used by a party to approve, cancel or reject a transaction instructed by the
counterparty.
This message cannot be used to request the modification of trade or event details.
The use of AdditionalInformation and its fields must be pre-agreed between account servicer and
account owner. The fields in that sequence cannot be used to amend a trade or event detail unless
authorised by country market practice.
Outline
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 783 March 2026
```

## File page 784

```text
The SecuritiesSettlementConditionsModificationRequestV10 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. AccountOwner
Party that legally owns the account.
B. SafekeepingAccount
Account to or from which a securities entry is made.
C. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
D. RequestDetails
Details of the request.
E. AdditionalInformation
Additional information that cannot be captured in the structured elements and/or any other specific
block.
F. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 784 March 2026
```

